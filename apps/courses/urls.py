from django.urls import path
from rest_framework import routers

from .views import CategoryViewSet, CourseViewSet, UploadCourseAPIView

app_name = 'courses'

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('upload/', UploadCourseAPIView.as_view(), name='upload'),
]
