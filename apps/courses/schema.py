from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from courses.models import Course


class CourseNode(DjangoObjectType):
    class Meta:
        model = Course
        interfaces = (Node,)
        filter_fields = [
            'name',
            'category',
            'school' ,
            'type',
            'price',
            'duration',
            'start_date',
            'certificate',
        ]


class Query(object):
    course = Node.Field(CourseNode)
    all_courses = DjangoFilterConnectionField(CourseNode)
