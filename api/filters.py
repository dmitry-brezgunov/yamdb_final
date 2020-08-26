from django_filters import rest_framework as filters

from .models import Title


class TitlesFilter(filters.FilterSet):
    '''Фильтрация произведения по названию, жанру, категории и году'''
    name = filters.CharFilter(field_name='name', lookup_expr='contains')
    genre = filters.CharFilter(field_name='genre__slug')
    category = filters.CharFilter(field_name='category__slug')

    class Meta:
        model = Title
        fields = ('name', 'category', 'genre', 'year')
