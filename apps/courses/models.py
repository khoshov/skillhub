from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.html import format_html
from django_extensions.db.fields import AutoSlugField
from meta.models import ModelMeta
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
import pymorphy2

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from pytils.translit import slugify

from courses.constants import ICONS_TEMPLATE

morph = pymorphy2.MorphAnalyzer(lang="ru")


class Course(models.Model):
    DRAFT = 1
    PUBLIC = 2
    STATUSES = (
        (DRAFT, _("Черновик")),
        (PUBLIC, _("Опубликован")),
    )

    ONLINE = 1
    OFFLINE = 2
    TYPE = (
        (ONLINE, _("Онлайн")),
        (OFFLINE, _("Оффлайн")),
    )

    BEGINNER = 1
    ADVANCED = 2
    DIFFICULTY = (
        (BEGINNER, _("С нуля")),
        (ADVANCED, _("Продвинутый")),
    )

    MISSING = 0
    LOW = 1
    INSIGNIFICANT = 2
    AVERAGE = 3
    SIGNIFICANT = 4
    HIGH = 5

    PRICE = (
        (MISSING, _("Бесплатно")),
        (LOW, _("Низкая цена")),
        (INSIGNIFICANT, _("Невысокая цена")),
        (AVERAGE, _("Средняя цена")),
        (SIGNIFICANT, _("Значительная цена")),
        (HIGH, _("Высокая цена")),
    )

    MONTH = 1
    LESSON = 2
    DURATION_TYPE = (
        (MONTH, _("Месяц")),
        (LESSON, _("Урок")),
    )

    name = RichTextField(
        _("Название"),
    )
    slug = AutoSlugField(
        _("Слаг"),
        populate_from="name",
        slugify_function=slugify,
        blank=True,
        null=True,
        # unique=True,
    )
    description = RichTextField(
        _("Описание"),
        blank=True,
        null=True,
    )
    url = models.URLField(
        _("Ссылка на страницу курса"),
    )
    affiliate_url = models.URLField(
        _("Партнёрская ссылка"), blank=True, null=True
    )
    categories = models.ManyToManyField(
        "courses.Category",
        through="courses.CourseCategory",
        verbose_name=_("Категория"),
    )
    school = models.ForeignKey(
        "schools.School",
        models.CASCADE,
        verbose_name=_("Школа"),
    )
    type = models.PositiveIntegerField(
        _("Тип"),
        choices=TYPE,
        default=ONLINE,
    )
    difficulty = models.PositiveIntegerField(
        _("Уровень сложности"),
        choices=DIFFICULTY,
        default=BEGINNER,
    )
    price = models.IntegerField(
        _("Цена ₽"),
        blank=True,
        null=True,
    )
    price_category = models.PositiveIntegerField(
        _("Категория цены"),
        choices=PRICE,
        default=AVERAGE,
    )
    duration = models.PositiveIntegerField(
        _("Длительность курсов"),
        blank=True,
        null=True,
    )
    duration_type = models.PositiveSmallIntegerField(
        _("Единицы измерения длительности курсов"),
        choices=DURATION_TYPE,
        default=MONTH,
    )
    duration_category = models.PositiveIntegerField(
        _("Категория продолжительности"),
        blank=True,
        null=True,
    )
    status = models.PositiveSmallIntegerField(
        _("Статус"),
        choices=STATUSES,
        default=DRAFT,
    )
    author = models.ForeignKey(
        get_user_model(),
        models.CASCADE,
        verbose_name=_("Автор"),
        related_name="courses",
        blank=True,
        null=True,
    )
    start_date = models.DateTimeField(
        _("Дата начала курсов"),
        blank=True,
        null=True,
    )
    installment = models.BooleanField(
        _("Возможна рассрочка"),
        default=False,
    )
    course_format = models.CharField(
        _("Формат проведения занятий"),
        max_length=255,
        default="Комбинированный",
    )
    deferred_payment = models.BooleanField(
        _("Возможен отложенный платёж"),
        default=False,
    )
    government_support = models.BooleanField(
        _("Гос. поддержка"),
        default=False,
    )
    recommended = models.BooleanField(
        _("Рекомендуем"),
        default=False,
    )
    created = models.DateTimeField(
        _("Дата создания"),
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        _("Дата обновлёния"),
        auto_now=True,
    )

    class Meta:
        db_table = "course"
        verbose_name = _("Курс")
        verbose_name_plural = _("Курсы")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("courses:detail", kwargs={"slug": self.slug})

    @property
    def price_formatted(self):
        if not self.price_category:
            return "Бесплатно"

        icons = "₽" * self.price_category
        missing_icons = "₽" * (5 - self.price_category)
        return format_html(ICONS_TEMPLATE.format(icons, missing_icons))

    @property
    def duration_formatted(self):
        duration_type = dict(Course.DURATION_TYPE)[self.duration_type].lower()
        duration_type = morph.parse(duration_type)[0]
        duration_type = duration_type.make_agree_with_number(
            self.duration
        ).word
        duration_html = f"{self.duration} {duration_type}"
        return format_html(duration_html)


class Category(ModelMeta, MPTTModel):
    parent = TreeForeignKey(
        "self",
        models.CASCADE,
        related_name="children",
        verbose_name=_("Родительская категория"),
        blank=True,
        null=True,
    )
    name = models.CharField(
        _("Имя"),
        max_length=255,
    )
    slug = AutoSlugField(
        _("Слаг"),
        populate_from="name",
        slugify_function=slugify,
        unique=True,
    )
    title = models.CharField(
        _("Заголовок"),
        max_length=255,
        blank=True,
        null=True,
    )
    description = RichTextField(
        _("Описание"),
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        _("Активный"),
        default=False,
    )
    sort_order = models.IntegerField(
        _("Сортировка"),
        default=0,
    )
    created = models.DateTimeField(
        _("created"),
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        _("updated"),
        auto_now=True,
    )

    extra_title = models.CharField(
        _("Дополнительный заголовок"),
        max_length=255,
        blank=True,
        null=True,
    )
    extra_text = RichTextField(
        _("Дополнительный текст"),
        blank=True,
        null=True,
    )

    meta_title = models.CharField(
        _("Meta title"),
        max_length=255,
        blank=True,
        null=True,
    )
    meta_description = models.TextField(
        _("Meta description"),
        blank=True,
        null=True,
    )

    _metadata = {
        "title": "meta_title",
        "description": "meta_description",
    }

    class Meta:
        db_table = "category"
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("courses:category", kwargs={"slug": self.slug})


class CourseCategory(models.Model):
    course = models.ForeignKey(
        "courses.Course",
        models.CASCADE,
    )
    category = models.ForeignKey(
        "courses.Category",
        models.CASCADE,
    )

    class Meta:
        db_table = "course_category"

    @property
    def course_count(self):
        categories = self.category.get_root().get_descendants(
            include_self=True
        )
        return Course.objects.filter(category__in=categories).count()


class CategoryAlias(models.Model):
    alias = models.CharField(
        _("Псевдоним категории"),
        max_length=255,
        unique=True,
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        verbose_name=_("категория"),
    )

    class Meta:
        verbose_name = _("Псевдоним категории")
        verbose_name_plural = _("Псевдонимы категорий")

    def __str__(self):
        return f"{self.alias} – {self.category.name}"
