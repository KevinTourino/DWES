from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PeliculaListAPIView, PeliculaDetailAPIView, PeliculaViewSet, UsuarioViewSet

# Router para ViewSets
router = DefaultRouter()
router.register('peliculas-viewset', PeliculaViewSet, basename='pelicula-viewset')
router.register('usuarios', UsuarioViewSet, basename='usuario')

urlpatterns = [
    # APIView (Bloque 2)
    path('api/peliculas/', PeliculaListAPIView.as_view(), name='pelicula-list'),
    path('api/peliculas/<int:pk>/', PeliculaDetailAPIView.as_view(), name='pelicula-detail'),
    
    # ViewSets (Bloque 3)
    path('api/', include(router.urls)),
]