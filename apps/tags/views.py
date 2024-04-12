from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny

from tags.models import Tag, TagMatch
from tags.serializers import TagMatchSerializer, TagSerializer


class TagMatchListCreateAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = TagMatchSerializer
    queryset = TagMatch.objects.all()


class TagListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
