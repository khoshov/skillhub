import django_tables2 as tables
from django.utils.html import format_html

from .models import Course

ICONS_TEMPLATE = '<span style="white-space: nowrap;">{}<span style="opacity: 0.15; -webkit-filter: grayscale(100%); filter: grayscale(100%);">{}</span></span>'


class CourseTable(tables.Table):
    school_rating = tables.Column(verbose_name='Рейтинг', accessor='school__rating')
    price_category = tables.Column(verbose_name='Цена', default='Бесплатно')
    duration_category = tables.Column(verbose_name='Длительность')

    class Meta:
        model = Course
        template_name = 'django_tables2/bootstrap4-responsive.html'
        fields = (
            'name',
            # 'url',
            # 'affiliate_url',
            # 'categories',
            'school',
            'school_rating',
            # 'type',
            # 'difficulty',
            # 'price',
            'price_category',
            'duration_category',
            # 'duration_type',
            # 'status',
            # 'author',
            # 'start_date',
            # 'installment',
            # 'course_format',
            # 'deferred_payment',
            # 'created',
        )

    def render_school_rating(self, value, record):
        icons = '⭐' * record.school.rating
        missing_icons = '⭐' * (5 - record.school.rating)
        return format_html(ICONS_TEMPLATE.format(icons, missing_icons))

    def render_price_category(self, value, record):
        icons = '💰' * record.price_category
        missing_icons = '💰️' * (5 - record.price_category)
        return format_html(ICONS_TEMPLATE.format(icons, missing_icons))

    def render_duration_category(self, value, record):
        icons = '⏳' * record.duration_category
        missing_icons = '⏳' * (5 - record.duration_category)
        return format_html(ICONS_TEMPLATE.format(icons, missing_icons))
