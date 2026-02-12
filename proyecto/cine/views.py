from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Pelicula, Usuario, Perfil, Genero, PeliculaGenero, Resena, Visualizacion
from .serializers import (
    PeliculaSerializer, UsuarioSerializer, PerfilSerializer,
    GeneroSerializer, PeliculaGeneroSerializer, ResenaSerializer,
    VisualizacionSerializer, MarcarVistaSerializer, CambioPrecioSerializer,
    AgregarResenaSerializer
)
from .filters import PeliculaFilter, ResenaFilter, UsuarioFilter
from .permissions import IsAuthenticatedForWrite


# ===== APIVIEW (Bloque 2) =====
class PeliculaListAPIView(APIView):
    permission_classes = [AllowAny]  # Público
    
    def get(self, request):
        peliculas = Pelicula.objects.all()
        serializer = PeliculaSerializer(peliculas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PeliculaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PeliculaDetailAPIView(APIView):
    permission_classes = [AllowAny]  # Público
    
    def get(self, request, pk):
        try:
            pelicula = Pelicula.objects.get(pk=pk)
            serializer = PeliculaSerializer(pelicula)
            return Response(serializer.data)
        except Pelicula.DoesNotExist:
            return Response(
                {'error': 'Pelicula no encontrada'},
                status=status.HTTP_404_NOT_FOUND
            )


# ===== VIEWSETS CON PROTECCIÓN JWT =====
class PeliculaViewSet(viewsets.ModelViewSet):
    """
    ViewSet de películas:
    - GET (lista/detalle): Público
    - POST/PUT/PATCH/DELETE: Requiere autenticación
    """
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PeliculaFilter
    search_fields = ['titulo', 'precio']
    ordering_fields = ['titulo', 'fecha_estreno', 'precio', 'duracion']
    ordering = ['titulo']
    permission_classes = [IsAuthenticatedOrReadOnly]  # Lectura pública, escritura autenticada
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def marcar_no_disponible(self, request, pk=None):
        """PROTEGIDA: Solo usuarios autenticados"""
        pelicula = self.get_object()
        
        if not pelicula.disponible:
            return Response(
                {'error': 'La pelicula ya esta marcada como no disponible'},
                status=status.HTTP_409_CONFLICT
            )
        
        pelicula.disponible = False
        pelicula.save()
        
        serializer = self.get_serializer(pelicula)
        return Response({
            'mensaje': 'Pelicula marcada como no disponible',
            'pelicula': serializer.data
        })
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def cambiar_precio(self, request, pk=None):
        """PROTEGIDA: Solo usuarios autenticados"""
        pelicula = self.get_object()
        serializer = CambioPrecioSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        precio_anterior = pelicula.precio
        pelicula.precio = serializer.validated_data['nuevo_precio']
        pelicula.save()
        
        return Response({
            'mensaje': 'Precio actualizado correctamente',
            'precio_anterior': str(precio_anterior),
            'precio_nuevo': str(pelicula.precio),
            'motivo': serializer.validated_data.get('motivo', 'Sin motivo especificado')
        })
    
    @action(detail=True, methods=['get'], permission_classes=[AllowAny])
    def estadisticas(self, request, pk=None):
        """PÚBLICA: Cualquiera puede ver estadísticas"""
        pelicula = self.get_object()
        
        resenas = Resena.objects.filter(pelicula=pelicula)
        visualizaciones = Visualizacion.objects.filter(pelicula=pelicula)
        
        if resenas.exists():
            promedio_puntuacion = sum(r.puntuacion for r in resenas) / resenas.count()
        else:
            promedio_puntuacion = 0
        
        return Response({
            'pelicula': pelicula.titulo,
            'total_resenas': resenas.count(),
            'promedio_puntuacion': round(promedio_puntuacion, 2),
            'total_visualizaciones': visualizaciones.count(),
            'minutos_totales_vistos': sum(v.minutos_vistos for v in visualizaciones)
        })
    
    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def destacadas(self, request):
        """PÚBLICA: Cualquiera puede ver películas destacadas"""
        peliculas_destacadas = []
        
        for pelicula in Pelicula.objects.filter(disponible=True):
            resenas = Resena.objects.filter(pelicula=pelicula)
            if resenas.exists():
                promedio = sum(r.puntuacion for r in resenas) / resenas.count()
                if promedio >= 4:
                    peliculas_destacadas.append({
                        'id': pelicula.id,
                        'titulo': pelicula.titulo,
                        'precio': str(pelicula.precio),
                        'promedio_puntuacion': round(promedio, 2)
                    })
        
        return Response(peliculas_destacadas)


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet de usuarios:
    - GET: Público
    - POST/PUT/PATCH/DELETE: Requiere autenticación
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = UsuarioFilter
    search_fields = ['username', 'email']
    ordering_fields = ['username', 'edad', 'created_at']
    ordering = ['username']
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def marcar_vista(self, request, pk=None):
        """PROTEGIDA: Solo usuarios autenticados pueden marcar visualizaciones"""
        usuario = self.get_object()
        
        pelicula_id = request.data.get('pelicula_id')
        if not pelicula_id:
            return Response(
                {'error': 'pelicula_id es requerido'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            pelicula = Pelicula.objects.get(pk=pelicula_id)
        except Pelicula.DoesNotExist:
            return Response(
                {'error': 'Pelicula no encontrada'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if not pelicula.disponible:
            return Response(
                {'error': 'Esta pelicula no esta disponible'},
                status=status.HTTP_409_CONFLICT
            )
        
        serializer = MarcarVistaSerializer(
            data=request.data,
            context={'pelicula': pelicula}
        )
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        visualizacion = Visualizacion.objects.create(
            usuario=usuario,
            pelicula=pelicula,
            minutos_vistos=serializer.validated_data['minutos_vistos'],
            fecha_visualizacion=serializer.validated_data.get(
                'fecha_visualizacion',
                timezone.now().date()
            )
        )
        
        return Response({
            'mensaje': 'Visualizacion registrada correctamente',
            'visualizacion': VisualizacionSerializer(visualizacion).data
        }, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['get'], permission_classes=[AllowAny])
    def historial(self, request, pk=None):
        """PÚBLICA: Cualquiera puede ver el historial"""
        usuario = self.get_object()
        visualizaciones = Visualizacion.objects.filter(usuario=usuario).order_by('-fecha_visualizacion')
        
        return Response({
            'usuario': usuario.username,
            'total_peliculas_vistas': visualizaciones.count(),
            'visualizaciones': VisualizacionSerializer(visualizaciones, many=True).data
        })


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class GeneroViewSet(viewsets.ModelViewSet):
    """Géneros: Lectura pública, escritura protegida"""
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nombre']
    ordering_fields = ['nombre']
    permission_classes = [IsAuthenticatedOrReadOnly]


class PeliculaGeneroViewSet(viewsets.ModelViewSet):
    queryset = PeliculaGenero.objects.all()
    serializer_class = PeliculaGeneroSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['pelicula', 'genero']
    ordering_fields = ['orden', 'fecha_asignacion']
    permission_classes = [IsAuthenticatedOrReadOnly]


class ResenaViewSet(viewsets.ModelViewSet):
    """Reseñas: Lectura pública, escritura protegida"""
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ResenaFilter
    search_fields = ['comentario']
    ordering_fields = ['fecha', 'puntuacion']
    ordering = ['-fecha']
    permission_classes = [IsAuthenticatedOrReadOnly]


class VisualizacionViewSet(viewsets.ModelViewSet):
    queryset = Visualizacion.objects.all()
    serializer_class = VisualizacionSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['usuario', 'pelicula']
    ordering_fields = ['fecha_visualizacion', 'minutos_vistos']
    permission_classes = [IsAuthenticatedOrReadOnly]