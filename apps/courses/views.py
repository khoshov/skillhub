from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey

from courses.filters import CategoryFilter, CourseFilter
from courses.models import Category, Course
from courses.serializers import CategorySerializer, CourseSerializer, CourseUploadSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filterset_class = CourseFilter


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(parent__isnull=True)
    filterset_class = CategoryFilter


class UploadCourseAPIView(APIView):
    permission_classes = [HasAPIKey]
    parser_classes = [JSONParser]

    # noinspection PyTypeChecker
    @swagger_auto_schema(auto_schema=None)
    def post(self, request):
        serializer = CourseUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
