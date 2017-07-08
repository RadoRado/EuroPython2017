import os

from celery import shared_task, chain, group


@shared_task(bind=True)
def debug_task(self):
    print(os.getpid())
    print('Request: {0!r}'.format(self.request))


@shared_task
def add(x, y):
    print('x={x}, y={y}'.format(x=x, y=y))

    return x + y


@shared_task
def task_signatures(n):
    add1 = add.s(x=1, y=n)
    add2 = add.s(x=2)

    add1.delay()
    add2.delay(y=n)


@shared_task
def task_chains(start, stop):
    """
    Tasks are executed one after another, sequentially
    Also defined as "chain of callbacks" -  [t1, t2, t3, ..., tn]
    t1 result will be passed to t2
    """
    tasks = [add.s(x=start, y=start)]

    while start < stop:
        start+= 1
        tasks.append(add.s(y=start))

    print(tasks)

    return chain(tasks).delay()


@shared_task
def task_groups(sums):
    """
    Tasks are executed in parallel. Order is not preserved
    """

    tasks = [add.s(x=x, y=y) for x, y in sums]
    print(tasks)

    return group(tasks).delay()


@shared_task
def task_group_with_chains(x, y, z):
    tasks = [task_chains.s(start=x, stop=10 * x),
             task_chains.s(start=y, stop=10 * y),
             task_chains.s(start=z, stop=10 * z)]

    return group(tasks).delay()
