from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pelicula


class PeliculaListAPIView(APIView):
    def get(self, request):
        peliculas = Pelicula.objects.all()
        data = []
        for pelicula in peliculas:
            data.append({
                'id': pelicula.id,
                'titulo': pelicula.titulo,
                'duracion': pelicula.duracion,
                'fecha_estreno': pelicula.fecha_estreno,
                'precio': str(pelicula.precio),
                'disponible': pelicula.disponible
            })
        return Response(data)

    def post(self, request):
        try:
            pelicula = Pelicula.objects.create(
                titulo=request.data.get('titulo'),
                duracion=request.data.get('duracion'),
                fecha_estreno=request.data.get('fecha_estreno'),
                precio=request.data.get('precio'),
                disponible=request.data.get('disponible', True)
            )
            data = {
                'id': pelicula.id,
                'titulo': pelicula.titulo,
                'duracion': pelicula.duracion,
                'fecha_estreno': pelicula.fecha_estreno,
                'precio': str(pelicula.precio),
                'disponible': pelicula.disponible
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class PeliculaDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            pelicula = Pelicula.objects.get(pk=pk)
            data = {
                'id': pelicula.id,
                'titulo': pelicula.titulo,
                'duracion': pelicula.duracion,
                'fecha_estreno': pelicula.fecha_estreno,
                'precio': str(pelicula.precio),
                'disponible': pelicula.disponible
            }
            return Response(data)
        except Pelicula.DoesNotExist:
            return Response(
                {'error': 'Pelicula no encontrada'},
                status=status.HTTP_404_NOT_FOUND
            )