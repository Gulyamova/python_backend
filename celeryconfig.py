from kombu import Exchange, Queue


BROKER_URL = 'pyamqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


CELERY_QUEUES = (
    Queue('queue1', Exchange('queue1'), routing_key='queue1'),
    Queue('queue2', Exchange('queue2'), routing_key='queue2'),
)


CELERY_IMPORTS = ('worker1', 'worker2')


CELERYD_CONCURRENCY = 2 
