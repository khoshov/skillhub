from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    name = models.CharField(
        _('Имя'),
        max_length=255,
    )

    class Meta:
        verbose_name = _('Метка')
        verbose_name_plural = _('Метки')

    def __str__(self):
        return self.name


class TagOption(models.Model):
    text = models.TextField(
        _('Текст'),
    )
    tag = models.ForeignKey(
        'tags.Tag',
        models.CASCADE,
        verbose_name=_('Метка'),
    )

    class Meta:
        verbose_name = _('Вариант метки')
        verbose_name_plural = _('Варианты меток')

    def __str__(self):
        return self.text


class TagMatch(models.Model):
    school = models.ForeignKey(
        'schools.School',
        models.CASCADE,
        verbose_name=_('Школа'),
    )
    review = models.ForeignKey(
        'reviews.Review',
        models.CASCADE,
        verbose_name=_('Отзыв'),
    )
    tag = models.ForeignKey(
        'tags.Tag',
        models.CASCADE,
        verbose_name=_('Метка'),
    )
    text = models.TextField(
        _('Текст'),
    )

    class Meta:
        verbose_name = _('Совпадение метки')
        verbose_name_plural = _('Совпадения меток')

    def __str__(self):
        return self.text
