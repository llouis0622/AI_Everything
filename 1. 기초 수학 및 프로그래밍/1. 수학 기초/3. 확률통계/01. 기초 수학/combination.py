def combination(n, x):
    res = factorial(n) / (factorial(x) * factorial(n - x))
    return res


def factorial(x):
    x_list = list(range(1, x + 1))
    res = 1
    for val in x_list:
        res *= val
    return res


combination(5, 3)