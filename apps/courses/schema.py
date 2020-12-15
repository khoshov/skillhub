from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from courses.models import Course


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
