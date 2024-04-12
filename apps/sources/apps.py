from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SourcesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sources'
    verbose_name = _('Источники данных')
