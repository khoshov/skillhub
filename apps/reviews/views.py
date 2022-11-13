from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey

from reviews.filters import ReviewFilter
from reviews.models import Review
from reviews.serializers import ReviewListSerializer, ReviewSerializer


class ReviewAPIView(APIView):
    permission_classes = [AllowAny]
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class ReviewListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ReviewListSerializer
    queryset = Review.objects.all()
    filterset_class = ReviewFilter
