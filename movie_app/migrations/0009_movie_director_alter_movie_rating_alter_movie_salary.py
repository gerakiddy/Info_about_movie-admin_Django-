# Generated by Django 4.1.3 on 2022-12-01 12:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0008_alter_movie_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='Квентин Тарантино', max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='salary',
            field=models.IntegerField(blank=True, default=1000000, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]