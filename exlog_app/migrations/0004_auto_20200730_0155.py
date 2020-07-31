# Generated by Django 3.0.7 on 2020-07-30 01:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exlog_app', '0003_auto_20200728_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exercise_name',
            field=models.CharField(max_length=32, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z\\s]*$', 'Only alphanumeric characters and dashes are allowed.')]),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_weight',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='num_reps',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='num_sets',
            field=models.PositiveIntegerField(),
        ),
    ]