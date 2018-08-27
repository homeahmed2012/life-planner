from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    content = models.CharField(max_length=100)
    question_type = models.CharField(max_length=1, default='a')


class Day(models.Model):
    date = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, through='DayQuestion', blank=True)

    def __str__(self):
        return str(self.date)


class Report(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    day = models.OneToOneField(Day, on_delete=models.CASCADE)


class Answer(models.Model):
    content = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class DayQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    value = models.IntegerField()



