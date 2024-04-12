from django.db.models import Q
from rest_framework import serializers

from schools.models import School, SchoolAlias


class SchoolSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    latest_review_url = serializers.URLField(allow_null=True)
    latest_review_published = serializers.DateField(allow_null=True)

    class Meta:
        model = School
        fields = (
            'name',
            'latest_review_url',
            'latest_review_published',
        )

    def get_name(self, obj):
        request = self.context.get('request')
        source = request.query_params.get('source')
        alias = None
        if source:
            alias = SchoolAlias.objects.filter(school=obj).filter(
                Q(source__name__icontains=source) |
                Q(source__url__icontains=source)
            ).first()
        return alias.name if alias else obj.name
