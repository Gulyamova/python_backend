from celery import Celery
from worker_1 import sum_numbers

app = Celery('producer', include=['worker1', 'worker2'])
app.config_from_object('celeryconfig')

if __name__ == '__main__':
    numbers = [12, 872, 13, 94, 231]
    result = sum_numbers.apply_async((numbers,))
    print("Task sent to calculate sum of numbers.")
