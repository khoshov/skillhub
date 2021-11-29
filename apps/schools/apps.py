from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SchoolsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schools'
    verbose_name = _('Школы')
