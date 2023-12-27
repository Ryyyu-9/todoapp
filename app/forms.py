from django import forms

from .models import Task

class TaskForm(forms.Form):
    # class Meta:
    #     model = Task
    #     # fields = ['task_name']
    #     # labels = {'task_name': 'Task Name'}
    #     # widgets = {'task_detail': forms.Textarea(attrs={'cols':80})}
    #     # labels = {'task_detail': 'Task detail'}
    task_name = forms.CharField(max_length=100)
    task_detail = forms.CharField(max_length=1000)
    parent_task_id = forms.IntegerField()
    cost_time = forms.TimeField()
