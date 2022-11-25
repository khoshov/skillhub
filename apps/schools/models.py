from ckeditor.fields import RichTextField

from django.db import models
from django.utils.translation import gettext_lazy as _


class School(models.Model):
    name = models.CharField(
        _('Название'),
        max_length=255,
    )
    description = RichTextField(
        _('Описание'),
        blank=True, null=True,
    )
    accredited = models.BooleanField(
        _('Аккредитованное учебное заведение'),
        default=False,
    )
    rating = models.FloatField(
        _('Рейтинг'),
        default=0,
    )
    epc = models.FloatField(
        _('Средний заработок с перехода'),
        default=0
    )
    is_active = models.BooleanField(
        _('Активный'),
        default=False,
    )

    class Meta:
        db_table = 'school'
        verbose_name = _('Школа')
        verbose_name_plural = _('Школы')

    def __str__(self):
        return self.name


class SchoolAlias(models.Model):
    name = models.CharField(
        _('Имя'),
        max_length=255,
    )
    school = models.ForeignKey(
        'schools.School',
        models.CASCADE,
        verbose_name=_('Школа'),
    )
    source = models.ForeignKey(
        'sources.DataSource',
        models.CASCADE,
        verbose_name=_('Источник данных'),
    )

    class Meta:
        verbose_name = _('Псевдоним школы')
        verbose_name_plural = _('Псевдонимы школ')

    def __str__(self):
        return self.name
