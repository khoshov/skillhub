from django.urls import path

from .views import TagMatchListCreateAPIView, TagListAPIView

app_name = 'reviews'

urlpatterns = [
    path('', TagMatchListCreateAPIView.as_view(), name='list'),
    path('match/', TagListAPIView.as_view(), name='match'),
]
