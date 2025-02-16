def derivative_x(f, x, step_size):
    m = (f(x + step_size) - f(x)) / ((x + step_size) - x)
    return m


def my_function(x):
    return x ** 2


slope_at_2 = derivative_x(my_function, 2, 0.00001)
print(slope_at_2)


def f(x):
    return x ** 2


def dx_f(x):
    return 2 * x


slope_at_2 = dx_f(2.0)
print(slope_at_2)