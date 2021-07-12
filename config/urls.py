from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from rest_framework import routers

from config.schema import schema
from courses.urls import router as courses_router
from schools.urls import router as schools_router

router = routers.DefaultRouter()
router.registry.extend(schools_router.registry)
router.registry.extend(courses_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('courses/', include('courses.urls', namespace='courses')),
    path('', include(router.urls)),
]
