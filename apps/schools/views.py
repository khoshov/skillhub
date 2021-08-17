from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey

from schools.filters import SchoolFilter
from schools.models import School
from schools.serializers import SchoolSerializer, FeedackUploadSerializer


class SchoolViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    filterset_class = SchoolFilter


class UploadFeedbackAPIView(APIView):
    permission_classes = [HasAPIKey]
    parser_classes = [JSONParser]

    # noinspection PyTypeChecker
    @swagger_auto_schema(auto_schema=None)
    def post(self, request):
        serializer = FeedackUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
