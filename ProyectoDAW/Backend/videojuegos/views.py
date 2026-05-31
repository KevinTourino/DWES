from django.shortcuts import render
from django.http import JsonResponse
from .service import fetch_igdb_games, fetch_igdb_games_id

from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import RegisterSerializer
from .filters import UserFilter

from .models import BibliotecaUsuario
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
    queryset = BibliotecaUsuario.objects.all()
    serializer_class = BibliotecaSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


