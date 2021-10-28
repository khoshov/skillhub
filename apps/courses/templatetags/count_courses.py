from django import template

from courses.models import Course

register = template.Library()


def count_courses(categories):
    return Course.objects.filter(
        categories__in=categories.values_list('id', flat=True),
    ).distinct().count()


register.filter('count_courses', count_courses)
