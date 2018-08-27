from django import forms
from day_app.models import Report


class ReportForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': '9'
        }
    ), label='التقرير اليومى')

    class Meta:
        model = Report
        fields = ['content']

