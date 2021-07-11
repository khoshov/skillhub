from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey

from courses.models import Course
from courses.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LoadCourseData(APIView):
    """
    обработчик post запросов парсера с данными о курсах
    """
    permission_classes = [HasAPIKey]
    parser_classes = [JSONParser]

    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            # сохраняем новый курс в базе или обновляем существующий
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            Response(serializer.errors, status=400)
