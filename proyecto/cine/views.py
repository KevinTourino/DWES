from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Pelicula, Usuario, Perfil, Genero, PeliculaGenero, Resena, Visualizacion
from .serializers import (
    PeliculaSerializer, UsuarioSerializer, PerfilSerializer,
    GeneroSerializer, PeliculaGeneroSerializer, ResenaSerializer,
    VisualizacionSerializer
)


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


# ===== VIEWSETS (Bloque 3 y 4) =====
class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer


class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class PeliculaGeneroViewSet(viewsets.ModelViewSet):
    queryset = PeliculaGenero.objects.all()
    serializer_class = PeliculaGeneroSerializer


class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer


class VisualizacionViewSet(viewsets.ModelViewSet):
    queryset = Visualizacion.objects.all()
    serializer_class = VisualizacionSerializer