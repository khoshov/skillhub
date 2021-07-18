from rest_framework import viewsets

from schools.filters import SchoolFilter
from schools.models import School
from schools.serializers import SchoolSerializer


class SchoolViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    filterset_class = SchoolFilter
