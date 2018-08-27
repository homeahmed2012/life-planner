from django.db import models
import datetime
from django.contrib.auth.models import User
from day_app.models import Day
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=6)  # add default and choices

    def __str__(self):
        return self.name


class Goal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    total_time = models.IntegerField()
    total_spend = models.IntegerField(default=0)
    is_done = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    goal_type = models.CharField(max_length=1, default='a')
    picture = models.ImageField(upload_to='goals_pics', null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE, blank=True)
    task_type = models.CharField(max_length=1, default='a')
    interval_form = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now)
    interval_to = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, blank=True)




