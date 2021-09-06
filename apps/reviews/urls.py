from django.urls import path

from reviews.views import ReviewAPIView

app_name = 'reviews'

urlpatterns = [
    path('upload/', ReviewAPIView.as_view(), name='upload'),
]
