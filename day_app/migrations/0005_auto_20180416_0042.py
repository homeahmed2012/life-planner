# Generated by Django 2.0.2 on 2018-04-15 22:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day_app', '0004_auto_20180416_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]