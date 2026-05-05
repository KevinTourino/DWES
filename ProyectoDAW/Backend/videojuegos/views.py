from django.shortcuts import render
from django.http import JsonResponse
from .service import fetch_igdb_games



def games_view(request):
    game_name = request.GET.get("name", "Zelda")

    data = fetch_igdb_games(game_name)
    return JsonResponse(data, safe=False)
