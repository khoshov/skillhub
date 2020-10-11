from django.db import models
from django.utils.translation import gettext_lazy as _


class School(models.Model):
    name = models.CharField(
        _('Название'),
        max_length=255,
    )
    description = models.TextField(
        _('Описание'),
        null=True, blank=True,
    )

    class Meta:
        db_table = 'school'
        verbose_name = _('Школа')
        verbose_name_plural = _('Школы')

    def __str__(self):
        return self.name
