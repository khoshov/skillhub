from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        permissions = (
            ('can_change_user_permissions', "Can change user permissions"),
        )
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return f'{self.email}'

    @classmethod
    def get_email_field_name(cls):
        return 'email'
