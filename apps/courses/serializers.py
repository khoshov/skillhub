from rest_framework import serializers

from courses.models import Category, Course, CategoryAlias
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
        try:
            category = CategoryAlias.objects.get(alias=category_alias).category
        except CategoryAlias.DoesNotExist:
            category = Category.objects.create(title=category_alias.capitalize())
            CategoryAlias.objects.create(
                alias=category_alias,
                category=category,
            )

        school = validated_data.pop('schcool')
        course, created = Course.objects.update_or_create(
            category=category,
            school=school,
            **validated_data
        )
        return course
