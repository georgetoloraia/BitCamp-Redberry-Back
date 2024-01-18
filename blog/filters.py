import django_filters
from .models import BlogModel

class CategoryFilter(django_filters.FilterSet):
    categories = django_filters.NumberFilter(field_name='categories', lookup_expr='id')

    class Meta:
        model = BlogModel
        fields = ['categories']
