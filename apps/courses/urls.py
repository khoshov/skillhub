from django.urls import path

from .views import CourseListView, UploadCourseAPIView, CourseDetailView

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('upload/', UploadCourseAPIView.as_view(), name='upload'),
    path('<slug:slug>/', CourseListView.as_view(), name='category'),
    path('courses/<slug:slug>', CourseDetailView.as_view(), name='detail'),
]
