from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('courses/', include('courses.urls', namespace='courses')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('schools/', include('schools.urls', namespace='schools')),

    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
