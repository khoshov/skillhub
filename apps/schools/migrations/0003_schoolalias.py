# Generated by Django 3.2.9 on 2022-11-25 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_school_epc'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolAlias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Псевдоним школы',
                'verbose_name_plural': 'Псевдонимы школ',
            },
        ),
    ]