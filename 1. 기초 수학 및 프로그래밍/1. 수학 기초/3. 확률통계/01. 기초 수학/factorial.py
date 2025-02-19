def factorial(x):
    x_list = list(range(1, x + 1))
    res = 1
    for val in x_list:
        res *= val
    return res


factorial(5)