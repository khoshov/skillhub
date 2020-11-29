import graphene
from graphene_django.debug import DjangoDebug

import courses.schema
import schools.schema


class Query(
    courses.schema.Query,
    schools.schema.Query,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query)
