from django import forms
from goal_app.models import Goal, Task, Comment
from django.utils.translation import gettext_lazy as _


class GoalForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': '6'
        }
    ), label='التفاصيل')
    date = forms.DateField(widget=forms.DateInput(), label='تاريخ الانتهاء')

    time = forms.CharField(widget=forms.TimeInput(), label='الوقت')

    class Meta:
        model = Goal
        exclude = ['user', 'picture', 'tags', 'finished_at', 'is_done']
        fields = ['title', 'description', 'total_time', 'total_spend',
                  'date', 'time', 'parent', 'goal_type']
        labels = {
            'title': _('الهدف '),
            'total_time': _('الوقت الكلى بالساعات '),
            'total_spend': _('الوقت المنقضى '),
            'parent': _('يتبع هدف ')
        }


class TaskForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': '6'
        }
    ), label='التفاصيل')

    date = forms.DateField(widget=forms.DateInput(), label='التاريخ')
    t_time = forms.CharField(widget=forms.TimeInput(), label='الوقت')

    class Meta:
        model = Task
        exclude = ['user',
                   'interval_form',
                   'interval_to',
                   'tags',
                   'day',
                   'time']
        fields = ['title', 'description', 'date', 't_time',
                  'duration', 'goal', 'task_type']
        labels = {
            'title': _('المهمة'),
            'duration': _('المدة بالدقائق'),
            'goal': _('يتبع هدف')
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']

