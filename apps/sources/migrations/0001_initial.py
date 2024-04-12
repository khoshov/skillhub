# Generated by Django 3.2.9 on 2022-11-25 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('url', models.URLField(verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Источник данных',
                'verbose_name_plural': 'Источники данных',
            },
        ),
    ]
