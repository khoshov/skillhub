# Generated by Django 3.2.9 on 2022-11-25 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_auto_20221125_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolalias',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aliases', to='schools.school', verbose_name='Школа'),
        ),
    ]