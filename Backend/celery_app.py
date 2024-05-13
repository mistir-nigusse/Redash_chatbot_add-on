from celery import Celery
import time

# Initialize Celery
app = Celery("tutorial", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")


@app.task
def add(x, y):
    time.sleep(5)
    return x + y


@app.task
def multiply(x, y):
    time.sleep(3)
    return x * y