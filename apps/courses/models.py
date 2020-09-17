from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Course(models.Model):
    ONLINE = 1
    OFFLINE = 2
    TYPES = [
        (ONLINE, _('Онлайн')),
        (OFFLINE, _('Оффлайн')),
    ]

    name = models.CharField(
        verbose_name=_('Название'),
        max_length=255,
    )
    category = models.ManyToManyField(
        to='courses.Category',
        through='courses.CourseCategory',
        verbose_name=_('Категория'),
    )
    school = models.ForeignKey(
        to='schools.School',
        on_delete=models.CASCADE,
        verbose_name=_('Школа'),
    )
    type = models.PositiveIntegerField(
        verbose_name=_('Тип'),
        choices=TYPES,
        default=ONLINE,
    )
    price = models.DecimalField(
        verbose_name=_('Цена ₽'),
        max_digits=9,
        decimal_places=2,
        null=True, blank=True,
    )
    duration = models.PositiveIntegerField(
        verbose_name=_('Длительность, мес.'),
        null=True, blank=True,
    )
    start_date = models.DateField(
        verbose_name=_('Дата старта'),
        null=True, blank=True,
    )
    certificate = models.BooleanField(
        verbose_name=_('Выдается сертификат гос. образца'),
        default=False,
    )

    class Meta:
        db_table = 'courses'
        verbose_name = _('Курс')
        verbose_name_plural = _('Курсы')

    def __str__(self):
        return self.name


class Category(MPTTModel):
    parent = TreeForeignKey(
        to='self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children',
        verbose_name=_('Родительская категория')
    )
    name = models.CharField(
        verbose_name=_('Имя'),
        max_length=255,
    )

    class Meta:
        db_table = 'categories'
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.name


class CourseCategory(models.Model):
    course = models.ForeignKey(
        to='courses.Course',
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        to='courses.Category',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'course_category'
