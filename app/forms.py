from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name']

    task_name = forms.CharField(max_length=100)
    task_detail = forms.CharField(max_length=1000)
    parent_task_id = forms.IntegerField(required=False)
    cost_time = forms.IntegerField(required=True)
    deadline_date = forms.DateTimeField(required=True)
