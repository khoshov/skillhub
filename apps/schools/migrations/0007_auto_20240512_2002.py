# Generated by Django 3.2.9 on 2024-05-12 20:02

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0006_schoolalias_disabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=255, populate_from='name', verbose_name='Слаг'),
        ),
        migrations.CreateModel(
            name='Disadvantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('order', models.IntegerField(default=0, verbose_name='Порядок')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disadvantages', to='schools.school', verbose_name='Школа')),
            ],
            options={
                'verbose_name': 'Недостаток школы',
                'verbose_name_plural': 'Недостатки школ',
            },
        ),
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('order', models.IntegerField(default=0, verbose_name='Порядок')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advantages', to='schools.school', verbose_name='Школа')),
            ],
            options={
                'verbose_name': 'Преимущество школы',
                'verbose_name_plural': 'Преимущества школ',
            },
        ),
    ]