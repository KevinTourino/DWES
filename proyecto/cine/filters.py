import django_filters
from .models import Pelicula, Resena, Usuario


class PeliculaFilter(django_filters.FilterSet):
    # Filtros simples por campos exactos
    disponible = django_filters.BooleanFilter()
    
    # Filtros avanzados - Rango de precios
    precio_min = django_filters.NumberFilter(field_name='precio', lookup_expr='gte')
    precio_max = django_filters.NumberFilter(field_name='precio', lookup_expr='lte')
    
    # Filtros avanzados - Rango de fechas
    fecha_desde = django_filters.DateFilter(field_name='fecha_estreno', lookup_expr='gte')
    fecha_hasta = django_filters.DateFilter(field_name='fecha_estreno', lookup_expr='lte')
    
    # Filtros avanzados - Duración mínima/máxima
    duracion_min = django_filters.NumberFilter(field_name='duracion', lookup_expr='gte')
    duracion_max = django_filters.NumberFilter(field_name='duracion', lookup_expr='lte')
    
    class Meta:
        model = Pelicula
        fields = ['disponible']


class ResenaFilter(django_filters.FilterSet):
    # Filtro simple
    puntuacion = django_filters.NumberFilter()
    
    # Filtro avanzado - Puntuación mínima/máxima
    puntuacion_min = django_filters.NumberFilter(field_name='puntuacion', lookup_expr='gte')
    puntuacion_max = django_filters.NumberFilter(field_name='puntuacion', lookup_expr='lte')
    
    # Filtro por rango de fechas
    fecha_desde = django_filters.DateFilter(field_name='fecha', lookup_expr='gte')
    fecha_hasta = django_filters.DateFilter(field_name='fecha', lookup_expr='lte')
    
    class Meta:
        model = Resena
        fields = ['puntuacion', 'usuario', 'pelicula']


class UsuarioFilter(django_filters.FilterSet):
    # Filtro simple
    activo = django_filters.BooleanFilter()
    
    # Filtro avanzado - Rango de edad
    edad_min = django_filters.NumberFilter(field_name='edad', lookup_expr='gte')
    edad_max = django_filters.NumberFilter(field_name='edad', lookup_expr='lte')
    
    class Meta:
        model = Usuario
        fields = ['activo']