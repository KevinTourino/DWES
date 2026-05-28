from django.shortcuts import render
from django.http import JsonResponse
from .service import fetch_igdb_games, fetch_igdb_games_id

from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RegisterSerializer
from .filters import UserFilter

from rest_framework import generics, permissions
from .models import Biblioteca
from .serializers import BibliotecaSerializer


def games_view(request):
    game_name = request.GET.get("name", "Zelda")

    data = fetch_igdb_games(game_name)
    return JsonResponse(data, safe=False)

def game_detail_view(request, id):
    data = fetch_igdb_games_id(id)
    return JsonResponse(data, safe=False)


class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserListView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    filterset_class = UserFilter











class BibliotecaCreateView(generics.CreateAPIView):

    serializer_class = BibliotecaSerializer

    permission_classes = [permissions.IsAuthenticated]


class BibliotecaListView(generics.ListAPIView):

    serializer_class = BibliotecaSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        return Biblioteca.objects.filter(
            usuario=self.request.user
        ).select_related(
            "videojuego"
        )
