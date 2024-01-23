import django_filters
from django_filters import rest_framework as filters
from .models import BlogModel, CategoryModel

class CategoryFilter(django_filters.FilterSet):
    # Filter that allows the user to filter blog posts by one or more category IDs
    categories = filters.ModelMultipleChoiceFilter(
        field_name='categories',
        queryset=CategoryModel.objects.all(),
        to_field_name='id',
        conjoined=False,  # Set to True if you want to enforce that the results must be in all the given categories
    )

    class Meta:
        model = BlogModel
        fields = ['categories']
