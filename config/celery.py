from celery import Celery


app = Celery('celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
