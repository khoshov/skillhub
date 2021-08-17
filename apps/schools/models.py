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

    class Meta:
        db_table = 'school'
        verbose_name = _('Школа')
        verbose_name_plural = _('Школы')

    def __str__(self):
        return self.name


class Feedback(models.Model):
    school = models.ForeignKey(
        'schools.School',
        models.CASCADE,
        verbose_name=_('Школа'),
    )
    feedback_source = models.CharField(
        _('Источник отзыва'),
        max_length=255,
    )
    feedback_url = models.URLField(
        _('Ссылка на отзыв'),
    )
    feedback_date = models.DateField(_('Дата публикации отзыва'))
    feedback_plus = models.TextField(
        _('Положительная часть отзыва'),
        blank=True, null=True,
    )
    feedback_minus = models.TextField(
        _('Отрицательная часть отзыва'),
        blank=True, null=True,
    )
    feedback_description = models.TextField(
        _('Основной текст отзыва'),
        blank=True, null=True,
    )

    class Meta:
        db_table = 'feedback'
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')

    def __str__(self):
        return f'feedback by url: {self.feedback_url}'
