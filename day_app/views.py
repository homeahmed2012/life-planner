from django.shortcuts import render, redirect
from django.http import HttpResponse
from goal_app.models import *
from day_app.forms import ReportForm

def all_days(request):
    user = request.user
    days = Day.objects.filter(user=user.id).order_by('date')
    return render(request, 'day_app/all_days.html', {'days': days})


def read_day(request, day_id):
    day = Day.objects.get(pk=day_id)
    user = request.user

    if day.user != user:
        return HttpResponse('you are not authorized to view this day.')

    tasks_a = Task.objects.filter(user=user.id,
                                  day=day.id,
                                  task_type='a').order_by('time')
    tasks_b = Task.objects.filter(user=user.id,
                                  day=day.id,
                                  task_type='b').order_by('time')

    report = ''
    if hasattr(day, 'report'):
        report = day.report

    return render(request, 'day_app/day.html', {'tasks_a': tasks_a,
                                                'tasks_b': tasks_b,
                                                'day': day,
                                                'report': report})


def create_report(request, day_id):
    day = Day.objects.get(pk=day_id)
    form = ReportForm()

    if request.method == 'POST':
        form = ReportForm(request.POST)

        if form.is_valid():
            report = form.save(commit=False)
            report.day = day
            report.save()
        return redirect('read_day', day.id)

    return render(request, 'day_app/create_report.html', {'form': form})


def update_report(request, day_id):
    day = Day.objects.get(pk=day_id)
    report = day.report

    form = ReportForm(instance=report)

    if request.method == 'POST':
        form = ReportForm(request.POST, instance=report)

        if form.is_valid():
            report = form.save(commit=False)
            report.day = day
            report.save()
        return redirect('read_day', day.id)

    return render(request, 'day_app/create_report.html', {'form': form})

# def create_day(request):
#     return HttpResponse('create_day')
#
#
#
#
# def update_day(request):
#     return HttpResponse('update_day')
#
#
# def delete_day(request):
#     return HttpResponse('delete_day')
#
#
# #  question
#
#
# def all_questions(request):
#     return HttpResponse('all_questions')
#
#
# def create_question(request):
#     return HttpResponse('create_question')
#
#
# def read_question(request):
#     return HttpResponse('read_question')
#
#
# def update_question(request):
#     return HttpResponse('update_question')
#
#
# def delete_question(request):
#     return HttpResponse('delete_question')
#
