# Generated by Django 2.0.2 on 2018-04-14 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal_app', '0003_auto_20180414_0038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='goal_id',
            new_name='goal',
        ),
        migrations.RenameField(
            model_name='goal',
            old_name='parent_id',
            new_name='parent',
        ),
        migrations.RenameField(
            model_name='goal',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='day_id',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='goal_id',
            new_name='goal',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='user_id',
            new_name='user',
        ),
    ]
