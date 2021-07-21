from django_filters import rest_framework as filters

from courses.models import Category, Course


class CourseFilter(filters.FilterSet):
    name__icontains = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Course
        fields = '__all__'


class CategoryFilter(filters.FilterSet):
    class Meta:
        model = Category
        fields = '__all__'
