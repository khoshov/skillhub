from django import template

from courses.tables import morph

register = template.Library()


@register.filter
def agree_with_number(value, num):
    print(value)
    print(num)
    return morph.parse(value)[0].make_agree_with_number(num).word
