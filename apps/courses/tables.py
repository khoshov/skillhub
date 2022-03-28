import django_tables2 as tables
import pymorphy2

from django.utils.html import format_html

from .models import Course

ICONS_TEMPLATE = '<span style="white-space: nowrap;">{}<span style="opacity: 0.15;">{}</span></span>'

morph = pymorphy2.MorphAnalyzer(lang='ru')


class CourseTable(tables.Table):
    name = tables.Column(verbose_name='Название курса', accessor='name')
    rating = tables.Column(verbose_name='Школа', accessor='school__rating', empty_values=())
    price = tables.Column(verbose_name='Цена', accessor='price_category', default='Бесплатно')
    duration = tables.Column(verbose_name='Длительность', accessor='duration_category', default='Нет данных')
    recommended = tables.Column(verbose_name='', accessor='recommended', default='')
    popularity = tables.Column(verbose_name='Популярность', accessor='popularity')
    url = tables.Column(verbose_name='Длительность', accessor='url')

    # duration_category = tables.Column(verbose_name='Длительность баллы')
    # popularity = tables.Column(verbose_name='Кол-во отзывов')

    class Meta:
        model = Course
        template_name = 'django_tables2/bootstrap4-responsive.html'
        order_by = '-popularity'
        fields = (
            'name',
            'rating',
            'duration',
            'price',
            'recommended',
            'popularity',

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
        rating_points = record.school.rating or 0
        rating_points_style = 'low-rating' if rating_points < 4 else 'high-rating'
        rating_icon_style = 'low-rating-icon' if rating_points < 4 else 'high-rating-icon'
        rating_icon = f'<span class="{rating_icon_style}"></span>'
        rating_tag = f'<span class="{rating_points_style}">{rating_points}</span>'
        rating = f'{rating_icon}{rating_tag}' if rating_points else ''
        return format_html(f'{record.school.name}{rating}')

    def render_price(self, value, record):
        if not record.price_category:
            return 'Бесплатно'

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

    def render_url(self, value, record):
        if record.affiliate_url:
            return record.affiliate_url
        return record.url

    def render_recommended(self, value, record):
        if record.recommended:
            icon = '<span class="recommended-icon"></span>'
            text = '<span class="recommended-text">Рекомендуем</span>'
            badge = f'<span class="recommended-badge>{icon}{text}</span>'
            return format_html(badge)
        else:
            return ''
