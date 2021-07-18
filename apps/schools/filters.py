from django_filters import rest_framework as filters

from schools.models import School


class SchoolFilter(filters.FilterSet):

    class Meta:
        model = School
        fields = '__all__'
