import graphene
from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from courses.models import Course, Category, CourseCategory


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (Node,)
        filter_fields = {
            "name": ["icontains", "exact"],
            "parent": ["exact", "isnull"],
        }


class CourseCategoryNode(DjangoObjectType):
    class Meta:
        model = CourseCategory
        interfaces = (Node,)
        filter_fields = {
            "course__name": ["exact"],
            "course__school": ["exact"],
            "course__type": ["exact"],
            "course__price": ["gt", "lt", "exact"],
            "course__duration": ["exact"],
            "course__start_date": ["gt", "lt", "exact"],
            "course__certificate": ["exact"],
            "category__parent": ["exact"],
            "category__name": ["exact"],
        }


class CourseNode(DjangoObjectType):
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
    course = Node.Field(CourseNode)
    all_courses = DjangoFilterConnectionField(CourseNode)

    category = Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    course_category = Node.Field(CourseCategoryNode)
    all_course_categories = DjangoFilterConnectionField(
        CourseCategoryNode,
        root_category=graphene.String()
    )

    def resolve_all_course_categories(self, info, root_category=None, **kwargs):
        print(root_category)
        return CourseCategory.objects.all()
