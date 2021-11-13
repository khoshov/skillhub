from django.db.models import Max, Min

from config.celery import app

from .models import Course


def apply_categories(courses, attribute_from, attribute_to, min_value, max_value):
    part = (max_value - min_value) / 5

    for course in courses:
        value = getattr(course, attribute_from)
        if value < min_value + part:
            setattr(course, attribute_to, Course.LOW)
        elif value < min_value + part * 2:
            setattr(course, attribute_to, Course.INSIGNIFICANT)
        elif value < min_value + part * 3:
            setattr(course, attribute_to, Course.AVERAGE)
        elif value < min_value + part * 4:
            setattr(course, attribute_to, Course.SIGNIFICANT)
        else:
            setattr(course, attribute_to, Course.HIGH)
        course.save()


@app.task
def aggregate_course_price():
    paid_courses = Course.objects.filter(price__isnull=False)
    free_courses = Course.objects.filter(price__isnull=True)

    free_courses.update(price_category=Course.MISSING)

    min_price = paid_courses.aggregate(Min('price'))['price__min']
    max_price = paid_courses.aggregate(Max('price'))['price__max']

    apply_categories(paid_courses, 'price', 'price_category', min_price, max_price)

@app.task
def aggregate_course_duration():
    courses_with_no_duration = Course.objects.filter(duration__isnull=True)
    courses_with_no_duration.update(duration_category=Course.MISSING)

    for duration_type in (Course.LESSON, Course.MONTH):
        courses = Course.objects.filter(duration__isnull=False, duration_type=duration_type)
        min_duration = courses.aggregate(Min('duration'))['duration__min']
        max_duration = courses.aggregate(Max('duration'))['duration__max']
        apply_categories(courses, 'duration', 'duration_category', min_duration, max_duration)
