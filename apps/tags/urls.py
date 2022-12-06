from django.urls import path

from .views import TagMatchListCreateAPIView, TagListAPIView

app_name = 'tags'

urlpatterns = [
    path('', TagListAPIView.as_view(), name='list'),
    path('match/', TagMatchListCreateAPIView.as_view(), name='match'),
]
