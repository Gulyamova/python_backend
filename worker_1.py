from celery import Celery
from celery.utils.log import get_task_logger

app = Celery('worker1')
app.config_from_object('celeryconfig')

logger = get_task_logger(__name__)


@app.task
def sum_numbers(numbers):
    logger.info(f"Received task to sum numbers: {numbers}")
    result = sum(numbers)
    return f"Sum of numbers: {result}"
