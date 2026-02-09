from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Pelicula, Usuario, Perfil, Genero, PeliculaGenero, Resena, Visualizacion
from .serializers import (
    PeliculaSerializer, UsuarioSerializer, PerfilSerializer,
    GeneroSerializer, PeliculaGeneroSerializer, ResenaSerializer,
    VisualizacionSerializer
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


# ===== VIEWSETS CON FILTROS, BÚSQUEDA, ORDENACIÓN (Bloque 3, 4 y 5) =====
class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PeliculaFilter
    search_fields = ['titulo', 'precio']
    ordering_fields = ['titulo', 'fecha_estreno', 'precio', 'duracion']
    ordering = ['titulo']


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = UsuarioFilter
    search_fields = ['username', 'email']
    ordering_fields = ['username', 'edad', 'created_at']
    ordering = ['username']


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