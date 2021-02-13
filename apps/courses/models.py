from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class DifficultyLevel(models.Model):
    name = models.CharField(
        _('Название'),
        max_length=255,
    )

    class Meta:
        db_table = 'difficulty_level'
        verbose_name = _('Уровень сложности')
        verbose_name_plural = _('Уровни сложности')

    def __str__(self):
        return self.name


class Course(models.Model):
    ONLINE = 1
    OFFLINE = 2
    TYPES = [
        (ONLINE, _('Онлайн')),
        (OFFLINE, _('Оффлайн')),
    ]

    name = models.CharField(
        _('Название'),
        max_length=255,
    )
    category = models.ManyToManyField(
        'courses.Category',
        through='courses.CourseCategory',
        verbose_name=_('Категория'),
    )
    school = models.ForeignKey(
        'schools.School',
        models.CASCADE,
        verbose_name=_('Школа'),
    )
    type = models.PositiveIntegerField(
        _('Тип'),
        choices=TYPES,
        default=ONLINE,
    )
    difficulty_level = models.ForeignKey(
        DifficultyLevel,
        models.CASCADE,
        verbose_name=_('Уровень сложности'),
    )
    duration = models.PositiveIntegerField(
        _('Длительность, мес.'),
        blank=True, null=True,
    )
    start_date = models.DateField(
        _('Дата старта'),
        null=True, blank=True,
    )
    price = models.DecimalField(
        _('Цена ₽'),
        max_digits=10,
        decimal_places=2,
        blank=True, null=True,
    )
    installment_price = models.DecimalField(
        _('Цена в рассрочку ₽'),
        max_digits=10,
        decimal_places=2,
        blank=True, null=True,
    )
    certificate = models.BooleanField(
        _('Выдается сертификат гос. образца'),
        default=False,
    )

    class Meta:
        db_table = 'course'
        verbose_name = _('Курс')
        verbose_name_plural = _('Курсы')

    def __str__(self):
        return self.name


class Category(MPTTModel):
    parent = TreeForeignKey(
        'self',
        models.CASCADE,
        related_name='children',
        verbose_name=_('Родительская категория'),
        blank=True, null=True,
    )
    name = models.CharField(
        _('Имя'),
        max_length=255,
    )
    description = models.TextField(
        _('Описание'),
        blank=True, null=True,
    )
    sort_order = models.IntegerField(
        _('Сортировка'),
        default=0,
    )

    class Meta:
        db_table = 'category'
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.name


class CourseCategory(models.Model):
    course = models.ForeignKey(
        'courses.Course',
        models.CASCADE,
    )
    category = models.ForeignKey(
        'courses.Category',
        models.CASCADE,
    )

    class Meta:
        db_table = 'course_category'

    @property
    def course_count(self):
        categories = self.category.get_root().get_descendants(include_self=True)
        return Course.objects.filter(category__in=categories).count()
