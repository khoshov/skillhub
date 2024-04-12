from django.urls import path

from reviews.views import ReviewAPIView, ReviewListAPIView, ReviewUpdateAPIView

app_name = 'reviews'

urlpatterns = [
    path('', ReviewListAPIView.as_view(), name='list'),
    path('<int:pk>/', ReviewUpdateAPIView.as_view(), name='update'),
    path('upload/', ReviewAPIView.as_view(), name='upload'),
]
