import random


def mc_expectation(sample_fn, f, n: int) -> float:
    s = 0.0
    for _ in range(n):
        s += f(sample_fn())
    return s / n


def mc_integral_1d(f, a: float, b: float, n: int) -> float:
    s = 0.0
    for _ in range(n):
        x = a + (b - a) * random.random()
        s += f(x)
    return (b - a) * (s / n)
