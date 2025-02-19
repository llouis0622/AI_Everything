def seq(start, stop, step):
    res = []
    current = start
    while current < stop:
        res.append(current)
        current += step
    return res


seq(2, 10, 1)