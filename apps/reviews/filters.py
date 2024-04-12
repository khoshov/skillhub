import django_filters

from .models import Review


class ReviewFilter(django_filters.FilterSet):
    school__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Review
        fields = [
            'school__name',
            'text_sentiment',
        ]
