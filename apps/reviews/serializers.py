from rest_framework import serializers

from reviews.models import Review
from schools.models import School


class ReviewSerializer(serializers.Serializer):
    school = serializers.CharField()
    feedback_source = serializers.CharField()
    feedback_url = serializers.URLField()
    feedback_date = serializers.DateField()
    feedback_plus = serializers.CharField(required=False, allow_null=True)
    feedback_minus = serializers.CharField(required=False, allow_null=True)
    feedback_description = serializers.CharField(required=False, allow_null=True)
    rating = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        school, _ = School.objects.get_or_create(name=validated_data.get('school'))

        review, _ = Review.objects.update_or_create(
            school=school,
            source=validated_data.get('feedback_source'),
            url=validated_data.get('feedback_url'),
            published=validated_data.get('feedback_date'),
            advantages=validated_data.get('feedback_plus'),
            disadvantages=validated_data.get('feedback_minus'),
            text=validated_data.get('feedback_description'),
            rating=validated_data.get('rating'),
        )
        return validated_data


class ReviewUpdateSerializer(serializers.ModelSerializer):
    school = serializers.CharField(source='school.name')

    class Meta:
        model = Review
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    school = serializers.CharField(source='school.name')

    class Meta:
        model = Review
        fields = '__all__'
