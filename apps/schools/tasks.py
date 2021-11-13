from django.db.models import Avg, F

from config.celery import app

from .models import School


@app.task
def aggregate_school_rating():
    schools = School.objects.annotate(average_rating=Avg('reviews__rating'))

    for school in schools:
        school.rating = round(school.average_rating or 0, 1)
        school.save()
