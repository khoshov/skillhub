from django.urls import path

from .views import LoadCourseData


urlpatterns = [
    path('upload/', LoadCourseData, name='upload_course_data'),
]