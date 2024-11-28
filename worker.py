from redis import Redis
from rq import Worker

from app.config import Configuration

config = Configuration()


def run_worker():
    """Picks tasks from the queue and runs them,
    storing back the results."""
    redis_connection = Redis(config.REDIS_HOST, config.REDIS_PORT)
    worker = Worker([config.QUEUE], connection=redis_connection)
    worker.work()


run_worker()
