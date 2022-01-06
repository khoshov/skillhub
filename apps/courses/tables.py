import django_tables2 as tables
import pymorphy2

from django.utils.html import format_html

from .models import Course

ICONS_TEMPLATE = '<span style="white-space: nowrap;">{}<span style="opacity: 0.15; -webkit-filter: grayscale(100%); filter: grayscale(100%);">{}</span></span>'

morph = pymorphy2.MorphAnalyzer(lang='ru')


class CourseTable(tables.Table):
    name = tables.Column(verbose_name='Название курса', accessor='name')
    rating = tables.Column(verbose_name='Школа', accessor='school__rating', empty_values=())
    price = tables.Column(verbose_name='Цена', accessor='price_category', default='Бесплатно')
    duration = tables.Column(verbose_name='Длительность', accessor='duration_category')
    url = tables.Column(verbose_name='Длительность', accessor='url')
    # duration_category = tables.Column(verbose_name='Длительность баллы')
    # popularity = tables.Column(verbose_name='Кол-во отзывов')

    class Meta:
        model = Course
        template_name = 'django_tables2/bootstrap4-responsive.html'
        fields = (
            'name',
            'rating',
            'price',
            'duration',
            # 'duration_category',
            # 'popularity',

            # 'affiliate_url',
            # 'author',
            # 'categories',
            # 'course_format',
            # 'created',
            # 'deferred_payment',
            # 'difficulty',
            # 'duration_type',
            # 'installment',
            # 'school_rating',
            # 'start_date',
            # 'status',
            # 'type',

            # should be the last one
            'url',
        )

    def render_rating(self, value, record):
        # rating = f'{record.school.rating}★' if record.school.rating else ''
        # return format_html(f'{record.school.name}&nbsp;{rating}')
        return record.school.name

    def render_price(self, value, record):
        icons = '₽' * record.price_category
        missing_icons = '₽' * (5 - record.price_category)
        return format_html(ICONS_TEMPLATE.format(icons, missing_icons))

    def render_duration(self, value, record):
        duration_type = dict(Course.DURATION_TYPE)[record.duration_type].lower()
        duration_type = morph.parse(duration_type)[0]
        duration_type = duration_type.make_agree_with_number(record.duration).word
        return f'{record.duration} {duration_type}'

    def render_duration_category(self, value, record):
        return record.duration_category
