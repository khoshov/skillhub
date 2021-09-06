from django import template

register = template.Library()


def next_page(value):
    return int(value) + 1


register.filter('next_page', next_page)
