# Generated by Django 2.1 on 2019-04-17 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal_app', '0010_auto_20190417_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='interval_form',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='interval_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]