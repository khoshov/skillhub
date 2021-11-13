import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from django.core.exceptions import DisallowedHost

from .base import *  # noqa

sentry_sdk.init(
    dsn="https://ba55c2cb70a742a591c8d389c4cd3748@o1056192.ingest.sentry.io/6042376",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,

    ignore_errors=[DisallowedHost],
)

CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
