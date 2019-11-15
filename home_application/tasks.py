from celery import task
from .views import plan

@task
def mul():
    print("任务开始____________")
    plan()
    print("任务结束____________")
    return True
