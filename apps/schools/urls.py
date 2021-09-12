from django.urls import path

from schools.views import SchoolListAPIView

app_name = 'schools'

urlpatterns = [
    path('', SchoolListAPIView.as_view(), name='list'),
]
