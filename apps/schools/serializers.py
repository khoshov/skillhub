from rest_framework import serializers

from schools.models import School


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


class SchoolAliasSerializer(serializers.ModelSerializer):
    school = serializers.CharField(source='school.name')
    source = serializers.CharField(source='source.name')

    class Meta:
        model = School
        fields = '__all__'
