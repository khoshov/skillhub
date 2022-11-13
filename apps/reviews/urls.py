from django.urls import path

from reviews.views import ReviewAPIView, ReviewListAPIView

app_name = 'reviews'

urlpatterns = [
    path('', ReviewListAPIView.as_view(), name='list'),
    path('upload/', ReviewAPIView.as_view(), name='upload'),
]
