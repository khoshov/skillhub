from django.db import models
from django.utils.translation import ugettext_lazy as _


class School(models.Model):
    name = models.CharField(
        verbose_name=_('Название'),
        max_length=255,
    )
    description = models.TextField(
        verbose_name=_('Описание'),
        null=True, blank=True,
    )

    class Meta:
        db_table = 'schools'
        verbose_name = _('Школа')
        verbose_name_plural = _('Школы')

    def __str__(self):
        return self.name
