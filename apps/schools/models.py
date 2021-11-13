from ckeditor.fields import RichTextField

from django.db import models
from django.utils.translation import gettext_lazy as _


class School(models.Model):
    MISSING = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    STARS = (
        (MISSING, _('Нет рейтинга')),
        (ONE, _('Одна звезда')),
        (TWO, _('Две звезды')),
        (THREE, _('Три звезды')),
        (FOUR, _('Четыре звезды')),
        (FIVE, _('Пять звёзд')),
    )

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
    rating = models.IntegerField(
        _('Рейтинг'),
        choices=STARS,
        default=THREE,
    )

    class Meta:
        db_table = 'school'
        verbose_name = _('Школа')
        verbose_name_plural = _('Школы')

    def __str__(self):
        return self.name
