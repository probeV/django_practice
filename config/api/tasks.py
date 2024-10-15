from typing import List
from celery import shared_task

@shared_task
def sum(a: int, b: int):
    print("test Celery task : ", a + b)
    return a+b

@shared_task
def mul(a: int, b: int):
    print("mul Celery task : ", a * b)
    return a*b

# @shared_task
# def test_periodic_task():
#     print("test Periodic task")
#     return "Complete"

