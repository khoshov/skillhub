from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from meta.models import ModelMeta
from solo.models import SingletonModel


class MainPageConfig(ModelMeta, SingletonModel):
    title = models.CharField(
        _('Заголовок'),
        max_length=255,
        blank=True, null=True,

    )
    description = models.TextField(
        _('Описание'),
        blank=True, null=True,
    )
    created = models.DateTimeField(
        _('created'),
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        _('updated'),
        auto_now=True,
    )

    meta_title = models.CharField(
        _('Meta title'),
        max_length=255,
        blank=True, null=True,
    )
    meta_description = models.TextField(
        _('Meta description'),
        blank=True, null=True,
    )

    _metadata = {
        'title': 'meta_title',
        'description': 'meta_description',
    }

    def __str__(self):
        return 'Главная страница'

    def get_absolute_url(self):
        return reverse('core:index')

    class Meta:
        verbose_name = _('Главная страница')


class AllCoursesPageConfig(ModelMeta, SingletonModel):
    title = models.CharField(
        _('Заголовок'),
        max_length=255,
        blank=True, null=True,

    )
    description = models.TextField(
        _('Описание'),
        blank=True, null=True,
    )

    meta_title = models.CharField(
        _('Meta title'),
        max_length=255,
        blank=True, null=True,
    )
    meta_description = models.TextField(
        _('Meta description'),
        blank=True, null=True,
    )

    _metadata = {
        'title': 'meta_title',
        'description': 'meta_description',
    }

    def __str__(self):
        return 'Страница всех курсов'

    class Meta:
        verbose_name = _('Страница всех курсов')
