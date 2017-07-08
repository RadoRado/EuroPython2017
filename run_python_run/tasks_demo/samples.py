def chain(tasks):
    results = []

    t1 = tasks[0]
    next_args = t1()

    results.append(next_args)

    for task in tasks[1:]:
        next_args = task(*next_args)
        results.append(next_args)

    return results

