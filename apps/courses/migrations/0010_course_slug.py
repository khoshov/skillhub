# Generated by Django 3.2.9 on 2023-11-11 17:03

import core.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=core.fields.AutoSlugField(populate_from='name', verbose_name='Слаг'),
        ),
    ]
