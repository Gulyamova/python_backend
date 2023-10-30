from celery import Celery
from celery.utils.log import get_task_logger

app = Celery('worker2')
app.config_from_object('celeryconfig')

logger = get_task_logger(__name__)


@app.task
def process_task2(message):
    logger.info(f"Received task for worker2: {message}")
    return f"Processed by worker2: {message}"
