from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Curso

class CursoListAPIView(APIView):
    def get(self, request):
        cursos = Curso.objects.all()

        data = []
        for curso in cursos:
            data.append({
                'id': curso.id,
                'titulo': curso.titulo,
                'precio': curso.precio,
                'nivel': curso.nivel
            })

        return Response(data)



class CursoDetalleAPIView(APIView):
    def get(self, request, pk):
        try:
            curso = Curso.objects.get(pk=pk)
        except Curso.DoesNotExist:
            return Response(
                {'error': 'Curso no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )

        data = {
            'id': curso.id,
            'titulo': curso.titulo,
            'precio': curso.precio,
            'nivel': curso.nivel
        }

        return Response(data)




class CursoCrerAPIView(APIView):
    def post(self, request):
        data = request.data

        if not data.get('titulo') or not data.get('precio') or not data.get('nivel'):
            return Response(
                {'error': 'Todos los campos son obligatorios'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if data['nivel'] not in ['principiante', 'intermedio', 'avanzado']:
            return Response(
                {'error': 'Nivel inválido'},
                status=status.HTTP_400_BAD_REQUEST
            )

        curso = Curso.objects.create(
            titulo=data['titulo'],
            precio=data['precio'],
            nivel=data['nivel']
        )

        return Response(
            {
                'id': curso.id,
                'titulo': curso.titulo,
                'precio': curso.precio,
                'nivel': curso.nivel
            },
            status=status.HTTP_201_CREATED
        )