import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from django.core.exceptions import DisallowedHost

from .base import *  # noqa

CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
