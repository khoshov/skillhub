from django_filters.views import FilterView
from django_tables2 import SingleTableView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from courses.filters import CourseFilter
from courses.models import Category, Course
from courses.serializers import CourseUploadSerializer
from courses.tables import CourseTable


class CourseListView(FilterView, SingleTableView):
    model = Course
    table_class = CourseTable
    template_name = 'courses/index.html'
    filterset_class = CourseFilter

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        category = self.request.GET.get('categories')
        if category:
            try:
                data['category'] = Category.objects.get(pk=int(category))
            except Category.DoesNotExist:
                pass
        return data


class UploadCourseAPIView(APIView):
    permission_classes = [AllowAny]
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = CourseUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
