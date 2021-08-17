from rest_framework import serializers

from schools.models import School, Feedback


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class FeedackUploadSerializer(serializers.Serializer):
    school = serializers.CharField()
    feedback_source = serializers.CharField()
    feedback_url = serializers.URLField()
    feedback_date = serializers.DateField()
    feedback_plus = serializers.CharField(required=False, allow_null=True)
    feedback_minus = serializers.CharField(required=False, allow_null=True)
    feedback_description = serializers.CharField(required=False, allow_null=True)

    def create(self, validated_data):
        school, _ = School.objects.get_or_create(name=validated_data.get('school'))

        course, _ = Feedback.objects.update_or_create(
            school=school,
            feedback_source=validated_data.get('feedback_source'),
            feedback_url=validated_data.get('feedback_url'),
            feedback_date=validated_data.get('feedback_date'),
            feedback_plus=validated_data.get('feedback_plus'),
            feedback_minus=validated_data.get('feedback_minus'),
            feedback_description=validated_data.get('feedback_description'),
        )
        return validated_data
