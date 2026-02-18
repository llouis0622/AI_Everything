import math
import random


def factorial(n: int) -> int:
    return math.factorial(n)


def nCk(n: int, k: int) -> int:
    return math.comb(n, k)


def arithmetic_sequence(a1: float, d: float, n: int):
    return [a1 + i * d for i in range(n)]


def geometric_sequence(a1: float, r: float, n: int):
    return [a1 * (r ** i) for i in range(n)]


def geometric_series_sum(a1: float, r: float, n: int) -> float:
    if r == 1:
        return a1 * n
    return a1 * (1 - r ** n) / (1 - r)


def infinite_geometric_series_sum(a: float, r: float) -> float:
    return a / (1 - r)


def is_monotone_increasing(xs, tol: float = 0.0) -> bool:
    return all(xs[i] <= xs[i + 1] + tol for i in range(len(xs) - 1))


def is_monotone_decreasing(xs, tol: float = 0.0) -> bool:
    return all(xs[i] + tol >= xs[i + 1] for i in range(len(xs) - 1))
