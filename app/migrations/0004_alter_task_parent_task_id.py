# Generated by Django 5.0 on 2024-01-02 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_task_parent_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='parent_task_id',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]