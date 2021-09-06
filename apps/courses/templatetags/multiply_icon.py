from django import template
register = template.Library()


@register.simple_tag()
def multiply_icon(icon, number):
    return icon * int(number)
