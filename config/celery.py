from celery import Celery
from celery.schedules import crontab

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'aggregate_course_price': {
        'task': 'courses.tasks.aggregate_price',
        'schedule': crontab(minute='*/1')
    },
}
