from django.db import models
from django.utils.translation import gettext_lazy as _


class DataSource(models.Model):
    name = models.CharField(
        _('Имя'),
        max_length=255,
    )
    url = models.URLField(
        _('Адрес'),
    )

    class Meta:
        verbose_name = _('Источник данных')
        verbose_name_plural = _('Источники данных')

    def __str__(self):
        return self.name
