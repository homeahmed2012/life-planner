from django.shortcuts import render, redirect
from goal_app.models import *
from goal_app.forms import GoalForm, TaskForm, CommentForm
from day_app.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def format_date_time(date, time):

    a = {'am': 0, 'pm': 12}
    h = int(time.split(':')[0]) + a[time[-2:]]
    h = ('' if h > 9 else '0') + str(h)
    m = time.split(':')[1][:-2]
    return str(date) + ' ' + h+':'+m+':00'
    # + '+02:00'


def add_time_to_parents(goal_id, duration):
    goal = Goal.objects.get(pk=goal_id.id)
    goal.total_spend += duration
    goal.save()
    if goal.parent:
        return add_time_to_parents(goal.parent, duration)


@login_required
def all_goals(request):
    user = request.user
    goals = Goal.objects.filter(user=user.id).order_by('-created_at')
    for goal in goals:
        goal.total_time //= 60
        goal.total_spend //= 60
    return render(request, 'goal_app/all_goals.html', {'goals': goals})


@login_required
def create_goal(request):
    form = GoalForm()
    user = request.user

    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = user
            goal.is_done = 0
            goal.total_time *= 60
            goal.finished_at = format_date_time(form.cleaned_data['date'],
                                                form.cleaned_data['time'])
            goal.save()
            return redirect('all_goals')
        else:
            print('form is not valid')

    form.fields['parent'].queryset = Goal.objects.filter(user=user.id)
    return render(request, 'goal_app/create_goal.html', {'form': form})


@login_required
def read_goal(request, goal_id):
    goal = Goal.objects.get(pk=goal_id)
    user = request.user
    if goal.user != user:
        return HttpResponse('you are not authorized to view this goal.')

    comments = Comment.objects.filter(goal=goal.id).order_by('created_at')
    goal.total_time //= 60
    goal.total_spend //= 60
    return render(request, 'goal_app/goal.html', {'goal': goal,
                                                  'comments': comments})


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
            goal.total_time *= 60
            goal.save()
            return redirect('read_goal', goal.id)
        else:
            print('form is not valid')
    form.fields['parent'].queryset = Goal.objects.filter(user=user.id)
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
    date_tasks = {}
    for task in tasks:
        if str(task.time.date()) in date_tasks:
            date_tasks[str(task.time.date())].append(task)
        else:
            date_tasks[str(task.time.date())] = [task]

    return render(request, 'goal_app/all_tasks.html', {'date_tasks': date_tasks})


@login_required
def create_task(request):
    form = TaskForm()
    user = request.user

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            day = Day.objects.get_or_create(date=form.cleaned_data['date'],
                                            user=user)[0]
            day.save()
            task.user = user
            task.day = day
            task.time = format_date_time(form.cleaned_data['date'],
                                         form.cleaned_data['t_time'])
            if task.task_type == 'b' and task.goal:
                add_time_to_parents(task.goal, task.duration)
            task.save()
            return redirect('all_tasks')
        else:
            print('form is not valid')

    form.fields['goal'].queryset = Goal.objects.filter(user=user.id)
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

    form.fields['goal'].queryset = Goal.objects.filter(user=user.id)
    return render(request, 'goal_app/create_task.html', {'form': form})


@login_required
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    user = request.user
    if task.user != user:
        return HttpResponse('you are not authorized to delete this task.')

    if task.task_type == 'b' and task.goal:
        add_time_to_parents(task.goal, -1 * task.duration)

    task.delete()
    return redirect('all_tasks')


def create_comment(request, goal_id):
    form = CommentForm()
    goal = Goal.objects.get(pk=goal_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.goal = goal

            comment.save()
            return redirect('read_goal', goal.id)
        else:
            print('form is not valid')

    return render(request, 'goal_app/create_comment.html', {'form': form})


def update_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    form = CommentForm(instance=comment)
    goal = Goal.objects.get(pk=comment.goal.id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.goal = goal

            comment.save()
            return redirect('read_goal', goal.id)
        else:
            print('form is not valid')

    return render(request, 'goal_app/create_comment.html', {'form': form})


def delete_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    goal = Goal.objects.get(pk=comment.goal.id)
    comment.delete()
    return redirect('read_goal', goal.id)


#
#
# def all_tags(request):
#     pass
