from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ReviewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'
    verbose_name = _('Отзывы')
