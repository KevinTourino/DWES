from django.shortcuts import render
from django.http import JsonResponse
from .service import fetch_igdb_games, fetch_igdb_games_id
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import RegisterSerializer
from .filters import UserFilter
from rest_framework.response import Response

from .models import BibliotecaUsuario, Videojuego
from .serializers import BibliotecaSerializer,EstadisticasBibliotecaSerializer, UltimoJuegoSerializer, MisJuegosSerializer, VideojuegoDetailSerializer




def games_view(request):
    game_name = request.GET.get("name", "Zelda")

    data = fetch_igdb_games(game_name)
    return JsonResponse(data, safe=False)

def game_detail_view(request, id):
    data = fetch_igdb_games_id(id)
    return JsonResponse(data, safe=False)


class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserListView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    filterset_class = UserFilter












class BibliotecaCreateView(generics.CreateAPIView):
    queryset = BibliotecaUsuario.objects.all()
    serializer_class = BibliotecaSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context
















class EstadisticasBibliotecaView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request):

        biblioteca = BibliotecaUsuario.objects.all()

        total_juegos = biblioteca.count()

        total_completados = biblioteca.filter(
            estado="completado"
        ).count()

        queryset = (
            BibliotecaUsuario.objects
            .select_related("videojuego")
            .prefetch_related("videojuego__generos")
            .order_by("-fecha_agregado")
        )

        vistos = set()
        ultimos_juegos = []

        for item in queryset:
            nombre = item.videojuego.nombre

            if nombre in vistos:
                continue

            vistos.add(nombre)
            ultimos_juegos.append(item)

            if len(ultimos_juegos) == 3:
                break

        serializer = EstadisticasBibliotecaSerializer({
            "total_juegos": total_juegos,
            "total_completados": total_completados,
            "ultimos_juegos": ultimos_juegos
        })

        return Response(serializer.data)
    






class MisJuegosView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MisJuegosSerializer

    def get(self, request):

        queryset = (
            BibliotecaUsuario.objects
            .filter(usuario=request.user)
            .select_related("videojuego")
            .prefetch_related("videojuego__generos")
            .order_by("-fecha_agregado")
        )

        vistos = set()
        filtrados = []

        for item in queryset:
            nombre = item.videojuego.nombre

            if nombre in vistos:
                continue

            vistos.add(nombre)
            filtrados.append(item)

        serializer = self.get_serializer(filtrados, many=True)

        return Response(serializer.data)
    






class VideojuegoDetailView(generics.RetrieveAPIView):
    serializer_class = VideojuegoDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return (
                BibliotecaUsuario.objects
                .select_related("videojuego", "plataforma")
                .prefetch_related("videojuego__generos")
                .get(
                    id=self.kwargs["id"],
                    usuario=self.request.user
                )
            )
        except BibliotecaUsuario.DoesNotExist:
            raise NotFound("Este juego no está en tu biblioteca")