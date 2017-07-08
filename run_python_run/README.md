# Run Python Run

This is the code for the `Django and Celery` training @ EuroPython 2017.

Requirements:

* Python `3.5.2` & should also work with `3.6.1`

To run:

1. `pip install -r requirement.txt`
2. `python manage.py migrate`
3. If you want to have Slack notifications, setup [Incoming Webhook](https://api.slack.com/incoming-webhooks)
4. `python manage.py runserver`


## Celery

In order to start celery, you need to execute the following command, at the level of `manage.py`:

```bash
$ celery -A run_python_run worker -E --loglevel=info
```

### Examples:

All examples are run in `python manage.py shell` with the following imports:

```python
from tasks_demo.tasks import add, task_signatures, task_chains, task_groups
```

Chains:

```python
task_chains(1, 10)
```

Groups:

```python
task_groups.delay([(x, x) for x in range(100)])
add.delay(1, 2).get()
```

Combining chains and groups:

```python
task_group_with_chains.delay(1, 2, 3)
```
