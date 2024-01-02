from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=50, null=False)
    task_detail = models.CharField(max_length=500, null=False)
    parent_task_id = models.IntegerField(max_length=10, null=True, blank=True)
    cost_time = models.IntegerField(null=True)
    deadline_date = models.DateField(null=True)
    register_date = models.DateTimeField(auto_now_add=True, null=False)
    update_date = models.DateTimeField(auto_now_add=True, null=False)
    is_deleted = models.BooleanField(null=True)

    def __str__(self) -> str:
        """task_nameを返す"""
        return self.task_name