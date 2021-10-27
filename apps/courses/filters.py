import django_filters

from .models import Category, Course


class CourseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    free = django_filters.BooleanFilter(field_name='price', lookup_expr='isnull')
    categories = django_filters.CharFilter(method='filter_by_category')

    class Meta:
        model = Course
        fields = [
            'name',
            'categories',
            'school',
            'school__rating',
            'price_category',
            'duration_category',
        ]

    def filter_by_category(self, queryset, name, value):
        categories = Category.objects.filter(pk=value).get_descendants(include_self=True)
        return queryset.filter(categories__in=categories).distinct()
