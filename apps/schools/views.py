from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from django.db.models import OuterRef, Subquery

from reviews.models import Review
from schools.models import School
from schools.serializers import SchoolSerializer


class SchoolListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = School.objects.annotate(
        latest_review_url=Subquery(
            Review.objects.filter(
                school_id=OuterRef('pk')
            ).order_by('-published').values('url')[:1]
        ),
        latest_review_published=Subquery(
            Review.objects.filter(
                school_id=OuterRef('pk')
            ).order_by('-published').values('published')[:1]
        ),
    )
    serializer_class = SchoolSerializer
