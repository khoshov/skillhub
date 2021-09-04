import django_filters

from .models import Course


class CourseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    free = django_filters.BooleanFilter(field_name='price', lookup_expr='isnull')

    class Meta:
        model = Course
        fields = ['name', 'categories']
