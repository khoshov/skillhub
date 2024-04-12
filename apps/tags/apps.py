from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TagsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tags'
    verbose_name = _('Метки')
