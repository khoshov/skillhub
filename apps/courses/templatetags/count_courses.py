from django import template

register = template.Library()


def count_courses(value):
    course_number = 0
    for category in value:
        course_number += category.course_set.count()
    return course_number


register.filter('count_courses', count_courses)
