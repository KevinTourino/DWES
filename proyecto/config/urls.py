from django.contrib import admin
from django.urls import path
from cine.views import PeliculaListAPIView, PeliculaDetailAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/peliculas/', PeliculaListAPIView.as_view(), name='pelicula-list'),
    path('api/peliculas/<int:pk>/', PeliculaDetailAPIView.as_view(), name='pelicula-detail'),
]