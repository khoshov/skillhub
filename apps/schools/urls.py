from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import SchoolViewSet, UploadFeedbackAPIView

router = DefaultRouter()

router.register(r'schools', SchoolViewSet, basename='school')

urlpatterns = [
    path('feedpack_upload/', UploadFeedbackAPIView.as_view(), name='feedback_upload'),
]