from celery import shared_task
from .models import Task

@shared_task
def notify_user_task_created(task_id):
    task = Task.objects.get(id=task_id)
    print(f"Email: Task '{task.title}' created for user '{task.user.username}'")
