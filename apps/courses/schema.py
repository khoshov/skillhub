import graphene
from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from courses.models import Category, Course, CourseCategory, DifficultyLevel


class DifficultyLevelNode(DjangoObjectType):
    class Meta:
        model = DifficultyLevel
        interfaces = (Node,)


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (Node,)
        filter_fields = {
            "name": ["icontains", "exact"],
            "parent": ["exact", "isnull"],
        }


class CourseCategoryNode(DjangoObjectType):
    course_count = graphene.Int()

    class Meta:
        model = CourseCategory
        interfaces = (Node,)
        filter_fields = {
            "course": ["exact"],
            "course__name": ["exact"],
            "category": ["exact"],
            "course__school": ["exact"],
            "course__type": ["exact"],
            "course__difficulty_level": ["exact"],
            "course__price": ["gt", "lt", "exact"],
            "course__duration": ["gt", "lt", "exact"],
            "course__start_date": ["gt", "lt", "exact"],
            "course__certificate": ["exact"],
            "category__parent": ["exact"],
            "category__name": ["exact"],
        }

    def resolve_course_count(self, info):
        return getattr(self, 'course_count', None)


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
            "duration": ["gt", "lt", "exact"],
            "start_date": ["gt", "lt", "exact"],
            "certificate": ["exact"],
        }


class Query(object):
    difficulty_level = Node.Field(DifficultyLevelNode)
    all_difficulty_levels = DjangoFilterConnectionField(DifficultyLevelNode)

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
        queryset = CourseCategory.objects.all()
        if root_category:
            categories = Category.objects.filter(name=root_category).get_descendants(include_self=True)
            print(categories)
            queryset = queryset.filter(category__in=categories)
        return queryset
