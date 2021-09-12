from rest_framework import serializers

from schools.models import School, Feedback


class SchoolSerializer(serializers.ModelSerializer):
    latest_review_url = serializers.URLField(allow_null=True)
    latest_review_published = serializers.DateField(allow_null=True)

    class Meta:
        model = School
        fields = (
            'name',
            'latest_review_url',
            'latest_review_published',
        )
