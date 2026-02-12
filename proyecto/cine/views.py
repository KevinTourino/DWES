from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.utils import timezone
from .models import Pelicula, Usuario, Perfil, Genero, PeliculaGenero, Resena, Visualizacion
from .serializers import (
    PeliculaSerializer, UsuarioSerializer, PerfilSerializer,
    GeneroSerializer, PeliculaGeneroSerializer, ResenaSerializer,
    VisualizacionSerializer, MarcarVistaSerializer, CambioPrecioSerializer,
    AgregarResenaSerializer
)
from .filters import PeliculaFilter, ResenaFilter, UsuarioFilter


# ===== APIVIEW (Bloque 2) =====
class PeliculaListAPIView(APIView):
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


# ===== VIEWSETS CON ACCIONES DE NEGOCIO =====
class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PeliculaFilter
    search_fields = ['titulo', 'precio']
    ordering_fields = ['titulo', 'fecha_estreno', 'precio', 'duracion']
    ordering = ['titulo']
    
    # ACCIÓN 1: Marcar película como no disponible (detail=True)
    @action(detail=True, methods=['post'])
    def marcar_no_disponible(self, request, pk=None):
        """
        Marca una película como no disponible.
        POST /api/peliculas-viewset/{id}/marcar_no_disponible/
        """
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
    
    # ACCIÓN 2: Cambiar precio con validación (detail=True)
    @action(detail=True, methods=['post'])
    def cambiar_precio(self, request, pk=None):
        """
        Cambia el precio de una película.
        POST /api/peliculas-viewset/{id}/cambiar_precio/
        Body: {"nuevo_precio": "15.99", "motivo": "Oferta especial"}
        """
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
    
    # ACCIÓN 3: Obtener estadísticas (detail=True)
    @action(detail=True, methods=['get'])
    def estadisticas(self, request, pk=None):
        """
        Obtiene estadísticas de una película.
        GET /api/peliculas-viewset/{id}/estadisticas/
        """
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
    
    # ACCIÓN 4: Películas destacadas (detail=False - colección)
    @action(detail=False, methods=['get'])
    def destacadas(self, request):
        """
        Obtiene películas con puntuación promedio >= 4.
        GET /api/peliculas-viewset/destacadas/
        """
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
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = UsuarioFilter
    search_fields = ['username', 'email']
    ordering_fields = ['username', 'edad', 'created_at']
    ordering = ['username']
    
    # ACCIÓN: Marcar película como vista (detail=True)
    @action(detail=True, methods=['post'])
    def marcar_vista(self, request, pk=None):
        """
        Registra que un usuario vio una película.
        POST /api/usuarios/{id}/marcar_vista/
        Body: {"pelicula_id": 1, "minutos_vistos": 120, "fecha_visualizacion": "2024-02-09"}
        """
        usuario = self.get_object()
        
        # Obtener pelicula_id del body
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
    
    # ACCIÓN: Historial de visualizaciones (detail=True)
    @action(detail=True, methods=['get'])
    def historial(self, request, pk=None):
        """
        Obtiene el historial de películas vistas por el usuario.
        GET /api/usuarios/{id}/historial/
        """
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


class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nombre']
    ordering_fields = ['nombre']


class PeliculaGeneroViewSet(viewsets.ModelViewSet):
    queryset = PeliculaGenero.objects.all()
    serializer_class = PeliculaGeneroSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['pelicula', 'genero']
    ordering_fields = ['orden', 'fecha_asignacion']


class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ResenaFilter
    search_fields = ['comentario']
    ordering_fields = ['fecha', 'puntuacion']
    ordering = ['-fecha']


class VisualizacionViewSet(viewsets.ModelViewSet):
    queryset = Visualizacion.objects.all()
    serializer_class = VisualizacionSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['usuario', 'pelicula']
    ordering_fields = ['fecha_visualizacion', 'minutos_vistos']