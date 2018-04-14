from django import forms
from goal_app.models import Goal, Task
from django.utils.translation import gettext_lazy as _


class GoalForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': '6'
        }
    ), label='التفاصيل')
    finished_at = forms.DateTimeField(widget=forms.DateTimeInput(
        attrs={
            'class': 'form-control',
            'position': 'relative'
        }
    ), label='ينتهى فى ')

    class Meta:
        model = Goal
        exclude = ['user', 'picture', 'tags']
        labels = {
            'title': _('الهدف '),
            'total_time': _('الوقت الكلى بالساعات '),
            'total_spend': _('الوقت المنقضى '),
            'is_done': _('تم انجازه '),
            'finished_at': _('ينتهى فى '),
            'parent': _('يتبع هدف ')
        }


class TaskForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': '6'
        }
    ), label='التفاصيل')

    class Meta:
        model = Task
        exclude = ['user',
                   'interval_form',
                   'interval_to',
                   'tags',
                   'day']
        labels = {
            'title': _('المهمة'),
            'time': _('الوقت'),
            'duration': _('المدة بالدقائق'),
            'goal': _('يتبع هدف')
        }




