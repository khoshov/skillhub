import django_tables2 as tables
import pymorphy2

from django.utils.html import format_html

from .models import Course

ICONS_TEMPLATE = '<span style="white-space: nowrap;">{}<span style="opacity: 0.15; -webkit-filter: grayscale(100%); filter: grayscale(100%);">{}</span></span>'

morph = pymorphy2.MorphAnalyzer(lang='ru')


class CourseTable(tables.Table):
    name = tables.Column(verbose_name='Название курса', accessor='name')
    price = tables.Column(verbose_name='Цена', accessor='price_category', default='Бесплатно')
    duration = tables.Column(verbose_name='Длительность', accessor='duration_category')
    popularity = tables.Column(verbose_name='Кол-во отзывов')

    # school_rating = tables.Column(verbose_name='Рейтинг школы', accessor='school__rating')
    # duration_category = tables.Column(verbose_name='Длительность')

    class Meta:
        model = Course
        template_name = 'django_tables2/bootstrap4-responsive.html'
        fields = (
            'name',
            'school',
            'price',
            'duration',

            # 'url',
            # 'affiliate_url',
            # 'categories',
            # 'school_rating',
            # 'type',
            # 'difficulty',
            # 'price',
            # 'duration_category',
            # 'duration_type',
            # 'status',
            # 'author',
            # 'start_date',
            # 'installment',
            # 'course_format',
            # 'deferred_payment',
            # 'created',
        )

    def render_school(self, value, record):
        return f'{value} {record.school.rating}★'

    def render_price(self, value, record):
        icons = '₽' * record.price_category
        missing_icons = '₽' * (5 - record.price_category)
        return format_html(ICONS_TEMPLATE.format(icons, missing_icons))

    def render_duration(self, value, record):
        duration_type = dict(Course.DURATION_TYPE)[record.duration_type].lower()
        duration_type = morph.parse(duration_type)[0]
        duration_type = duration_type.make_agree_with_number(record.duration).word
        return f'{record.duration} {duration_type}'
