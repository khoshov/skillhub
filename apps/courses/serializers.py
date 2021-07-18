from rest_framework import serializers

from courses.models import Category, Course, CategoryAlias, CourseCategory
from schools.models import School
from schools.serializers import SchoolSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    school = SchoolSerializer()
    type = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_type(self, obj):
        return obj.get_type_display()


class CourseUploadSerializer(serializers.Serializer):
    school = serializers.CharField()
    course_category = serializers.CharField()
    course_title = serializers.CharField()
    course_price = serializers.CharField(required=False, allow_null=True)
    course_start_date = serializers.DateField(required=False, allow_null=True)
    course_duration = serializers.FloatField()
    course_duration_type = serializers.FloatField()
    course_link = serializers.URLField()

    def create(self, validated_data):
        school, _ = School.objects.get_or_create(name=validated_data.get('school'))

        course, _ = Course.objects.update_or_create(
            name=validated_data.get('course_title'),
            url=validated_data.get('course_link'),
            school=school,
            price_details=validated_data.get('course_price'),
            duration=validated_data.get('course_duration'),
            duration_type=validated_data.get('course_duration_type'),
            start_date=validated_data.get('course_start_date'),
        )

        category_alias = validated_data.get('course_category')

        try:
            category = CategoryAlias.objects.get(alias=category_alias).category
        except CategoryAlias.DoesNotExist:
            category = Category.objects.create(name=category_alias.capitalize())
            CategoryAlias.objects.create(alias=category_alias, category=category)

        CourseCategory.objects.update_or_create(
            course=course,
            category=category,
        )

        return validated_data
