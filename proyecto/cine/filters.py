import django_filters
from .models import Pelicula, Resena, Usuario


class PeliculaFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains')
    precio_min = django_filters.NumberFilter(field_name='precio', lookup_expr='gte')
    precio_max = django_filters.NumberFilter(field_name='precio', lookup_expr='lte')
    disponible = django_filters.BooleanFilter(field_name='disponible')
    fecha_desde = django_filters.DateFilter(field_name='fecha_estreno', lookup_expr='gte')
    fecha_hasta = django_filters.DateFilter(field_name='fecha_estreno', lookup_expr='lte')

    class Meta:
        model = Pelicula
        fields = ['titulo', 'disponible', 'precio_min', 'precio_max']


class ResenaFilter(django_filters.FilterSet):
    puntuacion_min = django_filters.NumberFilter(field_name='puntuacion', lookup_expr='gte')
    puntuacion_max = django_filters.NumberFilter(field_name='puntuacion', lookup_expr='lte')
    pelicula = django_filters.NumberFilter(field_name='pelicula__id')
    usuario = django_filters.NumberFilter(field_name='usuario__id')

    class Meta:
        model = Resena
        fields = ['pelicula', 'usuario', 'puntuacion_min', 'puntuacion_max']


class UsuarioFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    activo = django_filters.BooleanFilter(field_name='activo')
    edad_min = django_filters.NumberFilter(field_name='edad', lookup_expr='gte')
    edad_max = django_filters.NumberFilter(field_name='edad', lookup_expr='lte')

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'activo']
