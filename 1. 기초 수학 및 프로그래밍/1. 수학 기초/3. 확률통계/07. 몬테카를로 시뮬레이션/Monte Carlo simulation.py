def seq(start, stop, step):
    res = []
    current = start
    while current < stop:
        res.append(current)
        current += step
    return res


def gamma_function(alpha, x):
    e = 2.7182817284
    res = (x ** (alpha - 1)) * (e ** (-x))
    return res


def gamma(alpha):
    a, b = 0, 100
    x_list = seq(0.0001, 100, 0.001)
    gamma_list = []
    for x in x_list:
        y = gamma_function(alpha, x)
        gamma_list.append(y)
    res = ((b - a) / len(x_list)) * sum(gamma_list)
    return res


gamma(3)