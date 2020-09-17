from rest_framework import serializers

from courses.models import Course
from schools.serializers import SchoolSerializer


class CourseSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()
    type = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_type(self, obj):
        return obj.get_type_display()
