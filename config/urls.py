from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework import routers

from config.schema import schema
from courses.urls import router as courses_router
from schools.urls import router as schools_router

schema_view = get_schema_view(
    openapi.Info(
        title="Skillhub API",
        default_version='v1',
        # description="Test description",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@snippets.local"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.registry.extend(schools_router.registry)
router.registry.extend(courses_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls', namespace='courses')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs'),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('', include(router.urls)),
]
