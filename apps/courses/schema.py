import graphene
from django.db.models import Q
from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from courses.models import Category, Course, CourseCategory


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
            "course__difficulty": ["exact"],
            "course__price": ["exact"],
            "course__duration": ["gt", "lt", "exact"],
            "course__start_date": ["exact"],
            "course__school__accredited": ["exact"],
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
            "categories": ["exact"],
            "school": ["exact"],
            "type": ["exact"],
            "price": ["exact"],
            "duration": ["gt", "lt", "exact"],
            "start_date": ["exact"],
            "school__accredited": ["exact"],
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
        queryset = CourseCategory.objects.all()
        if root_category:
            categories = Category.objects.filter(
                Q(name__icontains=root_category) | Q(slug__icontains=root_category)
            ).get_descendants(include_self=True)
            queryset = queryset.filter(category__in=categories)
        return queryset
