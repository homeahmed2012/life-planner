from django.contrib import admin
from goal_app.models import Tag, Goal, Task, Comment
# Register your models here.

admin.site.register(Tag)
admin.site.register(Goal)
admin.site.register(Task)
admin.site.register(Comment)
