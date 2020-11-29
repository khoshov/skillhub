from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from schools.models import School


class SchoolNode(DjangoObjectType):
    class Meta:
        model = School
        interfaces = (Node,)
        filter_fields = ['name',]


class Query(object):
    school = Node.Field(SchoolNode)
    all_schools = DjangoFilterConnectionField(SchoolNode)
