# Generated by Django 2.0.2 on 2018-04-14 00:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal_app', '0002_auto_20180414_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='finished_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
