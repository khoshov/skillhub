from config.celery import app

from .utils import aggregate_course_price


@app.task
def aggregate_price():
    aggregate_course_price()
