# Generated by Django 3.2.9 on 2022-07-13 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20220713_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='epc',
        ),
    ]
