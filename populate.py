import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

import random
from polls.models import Topic, Webpage
from goals.models import Goal
from tasks.models import Task
from feedback.models import Feedback
from faker import Faker


fakegen = Faker()

topics = ['ahmed', 'mohamed', 'ali', 'anas']


def populate_goals(N=5):
    for entry in range(N):
        title = fakegen.company()
        desc = fakegen.text()
        total_time = random.randint(1, 10)
        finish_time = fakegen.date_time()

        go = Goal.objects.get_or_create(title=title,
                                        description=desc,
                                        total_time=total_time,
                                        finished_at=finish_time,)[0]
        go.save()


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate_polls(N=5):

    for entry in range(N):

        top = add_topic()
        fake_name = fakegen.company()
        fake_url = fakegen.url()

        webg = Webpage.objects.get_or_create(category=top, name=fake_name, url=fake_url)[0]


def populate_feeds(N=5):

    for entry in range(N):
        text = fakegen.company()
        feed = Feedback.objects.get_or_create(text=text)[0]
        feed.save()


def populate_tasks(N=5):

    for entry in range(N):
        title = fakegen.company()
        desc = fakegen.text()
        date = fakegen.date_time()
        duration = random.randint(1, 60)

        go = Task.objects.get_or_create(title=title,
                                        description=desc,
                                        date=date,
                                        duration=duration)[0]
        go.save()


if __name__ == '__main__':
    print('woking')
    populate_tasks(10)
    print('done')