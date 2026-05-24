from django.shortcuts import render
from django.http import JsonResponse
from .service import fetch_igdb_games

from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RegisterSerializer
from .filters import UserFilter


def games_view(request):
    game_name = request.GET.get("name", "Zelda")

    data = fetch_igdb_games(game_name)
    return JsonResponse(data, safe=False)


class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserListView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    filterset_class = UserFilter
