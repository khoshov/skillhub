from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('admin/', admin.site.urls),

    path('courses/', include('courses.urls', namespace='courses')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('schools/', include('schools.urls', namespace='schools')),

    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    path('sentry-debug/', trigger_error),
]
