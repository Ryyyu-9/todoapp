from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('app/task=<int:task_id>/', views.task, name='task'),
    path('add_task/', views.add_task, name='add_task'),
]

