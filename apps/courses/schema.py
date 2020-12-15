from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from courses.models import Course, Category, CourseCategory


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (Node,)
        filter_fields = {
            "name": ["icontains", "exact"],
            "parent": ["exact"],
        }


class CourseCategoryType(DjangoObjectType):
    class Meta:
        model = CourseCategory
        interfaces = (Node,)
        filter_fields = {
            "course": ["exact"],
            "category": ["exact"],
        }


class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        interfaces = (Node,)
        filter_fields = {
            "name": ["icontains", "exact"],
            "category": ["exact"],
            "school": ["exact"],
            "type": ["exact"],
            "price": ["gt", "lt", "exact"],
            "duration": ["exact"],
            "start_date": ["gt", "lt", "exact"],
            "certificate": ["exact"],
        }


class Query(object):
    course = Node.Field(CourseType)
    all_courses = DjangoFilterConnectionField(CourseType)
