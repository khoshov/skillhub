from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from schools.models import School


class SchoolType(DjangoObjectType):
    class Meta:
        model = School
        interfaces = (Node,)
        filter_fields = ['name',]


class Query(object):
    school = Node.Field(SchoolType)
    all_schools = DjangoFilterConnectionField(SchoolType)
