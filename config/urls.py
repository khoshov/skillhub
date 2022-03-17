from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from core.views import page_not_found, server_error

urlpatterns = [
    path('admin/', admin.site.urls),

    path('courses/', include('courses.urls', namespace='courses')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('schools/', include('schools.urls', namespace='schools')),

    path('404/', TemplateView.as_view(template_name='404.html')),
    path('500/', TemplateView.as_view(template_name='500.html')),

    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
