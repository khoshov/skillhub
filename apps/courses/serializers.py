from rest_framework import serializers

from courses.models import Category, Course
from schools.serializers import SchoolSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    school = SchoolSerializer()
    type = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_type(self, obj):
        return obj.get_type_display()

    def create(self, validated_data):
        """
        функция создает или обновляет данные о курсее в базе данных на основе полученных
        проваледированных данных
        """
        category_alias = validated_data.pop('category')
        category = Category.objects.filter(category_alias__alias=category_alias)
        school = validated_data.pop('schcool')
        course, created = Course.objects.update_or_create(
            category=category,
            school=school,
            **validated_data
        )
        return course
