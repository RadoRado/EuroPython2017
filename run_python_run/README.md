# Run Python Run

This is the code for the `Django and Celery` training @ EuroPython 2017.

Requirements:

* Python `3.5.2` & should also work with `3.6.1`

To run:

1. `pip install -r requirement.txt`
2. `python manage.py migrate`
3. If you want to have Slack notifications, setup [Incoming Webhook](https://api.slack.com/incoming-webhooks)
4. `python manage.py runserver`
5. Create superuser for accessing the Django admin - `python manage.py createsuperuser`
6. Open `localhost:8000`
7. For real-time monitoring of Celery, you can use `flower` - <https://github.com/mher/flower> - `pip install flower` + `flower --port=5555`. Then open `localhost:5555`

The system is a simple "Online Python REPL" that uses a grader for running the Python code - <https://github.com/HackSoftware/HackGrader>

The grader location for EuroPython training is here - <https://st-grader.hackbulgaria.com/>

**For example purposes, this grader instance has no API authentication.**

## The task

**LOOK HERE**
```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

Your task is to turn this synchronous Django code into better-structured Django + Celery code.

All external calls should be done by Celery.

To do so, you can easily make another branch and work there.

```bash
$ git checkout -b solution
```

Celery tasks should be located in a `tasks.py` module in each app.

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```
**LOOK HERE**

## Celery

* You need RabbitMQ. For installation, [check here](http://www.rabbitmq.com/download.html)
* To start RabbitMQ management plugin, [check here](https://www.rabbitmq.com/management.html). This is not required to run Celery but gives nice overview of what's happening.

In order to start celery, you need to execute the following command, at the level of `manage.py`:

```bash
$ celery -A run_python_run worker -E --loglevel=info
```

### Examples:

All examples are run in `python manage.py shell` with the following imports:

```python
from tasks_demo.tasks import (
  add,
  task_signatures,
  task_chains,
  task_groups,
  task_group_with_chains,
  retry_task,
  task_blocker,
  remote_task_debugger
)
```

**Chains:**

```python
task_chains(1, 10)
```

**Groups:**

```python
task_groups.delay([(x, x) for x in range(100)])
add.delay(1, 2).get()
```

**Combining chains and groups:**

```python
task_group_with_chains.delay(1, 2, 3)
```

**Task retrying:**

```python
retry_task.delay()
```

**Block everything:**

```python
task_blocker.delay()
task_blocker.delay()
task_blocker.delay()
task_blocker.delay()

add.delay(1, 2)
```

**Remote task debugging:**

```python
remote_task_debugger.delay()
```

Then see celery log for port and:

```bash
$ telnet localhost 6900  # pick the port from logs
```

### Additional resources

* [First steps with Celery](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html)
* [First steps with Django](http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)
* [Using RabbitMQ as broker](http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html)
* [Logging](http://docs.celeryproject.org/en/latest/userguide/tasks.html#logging)
