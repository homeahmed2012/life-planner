from django.contrib import admin
from day_app.models import Question, Day, Report, Answer, DayQuestion
# Register your models here.

admin.site.register(Question)
admin.site.register(Day)
admin.site.register(Report)
admin.site.register(Answer)
admin.site.register(DayQuestion)
