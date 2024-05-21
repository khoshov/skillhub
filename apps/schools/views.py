from django.db.models import OuterRef, Q, Subquery
from django.views.generic import DetailView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from courses.models import Course
from reviews.models import Review
from schools.models import School, SchoolAlias
from schools.serializers import SchoolSerializer


class SchoolDetailView(DetailView):
    model = School
    template_name = "schools/detail.html"
    context_object_name = "school"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.filter(school=self.object)

        return context


class SchoolListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = SchoolSerializer

    def get_queryset(self):
        qs = School.objects.filter(is_active=True).annotate(
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

        source = self.request.query_params.get('source')

        if source:
            contains_source = (
                Q(source__name__icontains=source) |
                Q(source__url__icontains=source)
            )
            disabled = Q(disabled=True)
            schools_ids = SchoolAlias.objects.filter(
                contains_source & disabled
            ).values_list('school_id', flat=True)

            qs = qs.exclude(id__in=schools_ids)

        return qs
