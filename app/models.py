from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=50)
    task_detail = models.CharField(max_length=500)
    parent_task_id = models.IntegerField(max_length=10)
    cost_time = models.TimeField()
    deadline_date = models.DateField()
    register_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()

    def __str__(self) -> str:
        """task_nameを返す"""
        return self.task_name