from django.shortcuts import render, redirect
from goal_app.models import *
from goal_app.forms import GoalForm, TaskForm
from day_app.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def all_goals(request):
    user = request.user
    goals = Goal.objects.filter(user=user.id).order_by('-created_at')
    return render(request, 'goal_app/all_goals.html', {'goals': goals})


@login_required
def create_goal(request):
    form = GoalForm()

    if request.method == 'POST':
        form = GoalForm(request.POST)
        user = request.user
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = user
            goal.save()
            return redirect('all_goals')
        else:
            print('form is not valid')

    return render(request, 'goal_app/create_goal.html', {'form': form})


@login_required
def read_goal(request, goal_id):
    goal = Goal.objects.get(pk=goal_id)
    user = request.user
    if goal.user != user:
        return HttpResponse('you are not authorized to view this goal.')

    return render(request, 'goal_app/goal.html', {'goal': goal})


@login_required
def update_goal(request, goal_id):
    goal = Goal.objects.get(pk=goal_id)
    user = request.user
    if goal.user != user:
        return HttpResponse('you are not authorized to edit this goal.')

    form = GoalForm(instance=goal)

    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)

        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = user
            goal.save()
            return redirect('read_goal', goal.id)
        else:
            print('form is not valid')

    return render(request, 'goal_app/create_goal.html', {'form': form})


@login_required
def delete_goal(request, goal_id):
    goal = Goal.objects.get(pk=goal_id)
    user = request.user
    if goal.user != user:
        return HttpResponse('you are not authorized to delete this goal.')

    goal.delete()
    return redirect('all_goals')


@login_required
def all_tasks(request):
    user = request.user
    tasks = Task.objects.filter(user=user.id).order_by('-time')
    return render(request, 'goal_app/all_tasks.html', {'tasks': tasks})


@login_required
def create_task(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        user = request.user

        if form.is_valid():
            task = form.save(commit=False)
            day = Day(date=form.cleaned_data['time'].date(),
                      user=user)
            day.save()
            task.user = user
            task.day = day
            task.save()
            return redirect('all_tasks')
        else:
            print('form is not valid')

    return render(request, 'goal_app/create_task.html', {'form': form})


@login_required
def read_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    user = request.user

    if task.user != user:
        return HttpResponse('you are not authorized to view this task.')

    goal_name = ' لا يوجد'
    if task.goal:
        goal = Goal.objects.get(pk=task.goal.id)
        goal_name = goal.title

    return render(request, 'goal_app/task.html', {'task': task, 'goal_name': goal_name})


@login_required
def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    user = request.user
    if task.user != user:
        return HttpResponse('you are not authorized to edit this task.')

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.save()
            return redirect('read_task', task.id)
        else:
            print('form is not valid')

    return render(request, 'goal_app/create_task.html', {'form': form})


@login_required
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    user = request.user
    if task.user != user:
        return HttpResponse('you are not authorized to delete this task.')

    task.delete()
    return redirect('all_tasks')

#
# def create_comment(request):
#     pass
#
#
# def update_comment(request):
#     pass
#
#
# def delete_comment(request):
#     pass
#
#
# def all_tags(request):
#     pass