from django.urls import path

from .views import CourseListView, UploadCourseAPIView

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('upload/', UploadCourseAPIView.as_view(), name='upload'),
]
