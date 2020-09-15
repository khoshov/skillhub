from django_filters import rest_framework as filters

from courses.models import Course


class CourseFilter(filters.FilterSet):

    class Meta:
        model = Course
        fields = ['category']
