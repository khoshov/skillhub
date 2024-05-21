from django.urls import path

from schools.views import SchoolListAPIView, SchoolDetailView

app_name = 'schools'

urlpatterns = [
    path('', SchoolListAPIView.as_view(), name='list'),
    path('<int:pk>/', SchoolDetailView.as_view(), name='detail'),
]
