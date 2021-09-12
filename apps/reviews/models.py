from django.db import models
from django.utils.translation import gettext_lazy as _


class Review(models.Model):
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

    school = models.ForeignKey(
        'schools.School',
        models.CASCADE,
        related_name='reviews',
        verbose_name=_('Школа'),
    )
    source = models.CharField(
        _('Источник отзыва'),
        max_length=255,
    )
    url = models.URLField(
        _('Ссылка на отзыв'),
    )
    published = models.DateField(
        _('Дата публикации отзыва'),
    )
    rating = models.IntegerField(
        _('Рейтинг'),
        choices=STARS,
        default=MISSING,
    )
    advantages = models.TextField(
        _('Положительная часть отзыва'),
        blank=True, null=True,
    )
    disadvantages = models.TextField(
        _('Отрицательная часть отзыва'),
        blank=True, null=True,
    )
    text = models.TextField(
        _('Основной текст отзыва'),
        blank=True, null=True,
    )

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')

    def __str__(self):
        return self.url
