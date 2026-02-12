from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PeliculaListAPIView, PeliculaDetailAPIView,
    PeliculaViewSet, UsuarioViewSet,
    PerfilViewSet, GeneroViewSet, PeliculaGeneroViewSet,
    ResenaViewSet, VisualizacionViewSet
)

# Router para ViewSets
router = DefaultRouter()
router.register('peliculas-viewset', PeliculaViewSet, basename='pelicula-viewset')
router.register('usuarios', UsuarioViewSet, basename='usuario')
router.register('perfiles', PerfilViewSet, basename='perfil')
router.register('generos', GeneroViewSet, basename='genero')
router.register('pelicula-generos', PeliculaGeneroViewSet, basename='pelicula-genero')
router.register('resenas', ResenaViewSet, basename='resena')
router.register('visualizaciones', VisualizacionViewSet, basename='visualizacion')

urlpatterns = [
    # APIView
    path('api/peliculas/', PeliculaListAPIView.as_view(), name='pelicula-list'),
    path('api/peliculas/<int:pk>/', PeliculaDetailAPIView.as_view(), name='pelicula-detail'),

    # ViewSets
    path('api/', include(router.urls)),
]