from django.db.models import Avg, F

from config.celery import app

from .models import School


@app.task
def aggregate_school_rating():
    schools = School.objects.annotate(average_rating=Avg('reviews__rating'))

    for school in schools:
        school.rating = school.average_rating
        school.save()
