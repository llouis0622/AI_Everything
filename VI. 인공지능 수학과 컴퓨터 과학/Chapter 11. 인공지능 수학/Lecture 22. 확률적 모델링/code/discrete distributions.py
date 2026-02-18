import math
import random


def factorial(n: int) -> int:
    return math.factorial(n)


def nCk(n: int, k: int) -> int:
    return math.comb(n, k)


def pmf_discrete_uniform(a: int, b: int):
    n = b - a + 1

    def f(x: int) -> float:
        if a <= x <= b:
            return 1.0 / n
        return 0.0

    return f


def mean_discrete_uniform(a: int, b: int) -> float:
    return (a + b) / 2.0


def var_discrete_uniform(a: int, b: int) -> float:
    n = b - a + 1
    return (n * n - 1) / 12.0


def bernoulli(p: float) -> int:
    return 1 if random.random() < p else 0


def pmf_bernoulli(x: int, p: float) -> float:
    if x == 1:
        return p
    if x == 0:
        return 1 - p
    return 0.0


def mean_bernoulli(p: float) -> float:
    return p


def var_bernoulli(p: float) -> float:
    return p * (1 - p)


def pmf_binomial(x: int, n: int, p: float) -> float:
    if x < 0 or x > n:
        return 0.0
    return nCk(n, x) * (p ** x) * ((1 - p) ** (n - x))


def mean_binomial(n: int, p: float) -> float:
    return n * p


def var_binomial(n: int, p: float) -> float:
    return n * p * (1 - p)


def mgf_binomial(t: float, n: int, p: float) -> float:
    return (p * math.exp(t) + (1 - p)) ** n


def pmf_poisson(x: int, lam: float) -> float:
    if x < 0:
        return 0.0
    return math.exp(-lam) * (lam ** x) / factorial(x)


def mean_poisson(lam: float) -> float:
    return lam


def var_poisson(lam: float) -> float:
    return lam


def mgf_poisson(t: float, lam: float) -> float:
    return math.exp(lam * (math.exp(t) - 1.0))


def poisson_approx_binomial(x: int, n: int, p: float) -> float:
    return pmf_poisson(x, n * p)


def geometric_trials(p: float) -> int:
    x = 1
    while True:
        if random.random() < p:
            return x
        x += 1


def pmf_geometric_trials(x: int, p: float) -> float:
    if x < 1:
        return 0.0
    return p * ((1 - p) ** (x - 1))


def cdf_geometric_trials(x: int, p: float) -> float:
    if x < 1:
        return 0.0
    return 1 - ((1 - p) ** x)


def mean_geometric_trials(p: float) -> float:
    return 1.0 / p


def var_geometric_trials(p: float) -> float:
    return (1 - p) / (p * p)


def pmf_geometric_failures(y: int, p: float) -> float:
    if y < 0:
        return 0.0
    return p * ((1 - p) ** y)


def mean_geometric_failures(p: float) -> float:
    return (1 - p) / p


def var_geometric_failures(p: float) -> float:
    return (1 - p) / (p * p)


def mgf_geometric_trials(t: float, p: float) -> float:
    denom = 1 - (1 - p) * math.exp(t)
    return p * math.exp(t) / denom


def negbin_trials(r: int, p: float) -> int:
    s = 0
    n = 0
    while s < r:
        n += 1
        s += bernoulli(p)
    return n


def pmf_negbin_trials(x: int, r: int, p: float) -> float:
    if x < r:
        return 0.0
    return nCk(x - 1, r - 1) * (p ** r) * ((1 - p) ** (x - r))


def mean_negbin_trials(r: int, p: float) -> float:
    return r / p


def var_negbin_trials(r: int, p: float) -> float:
    return r * (1 - p) / (p * p)


def pmf_negbin_failures(y: int, r: int, p: float) -> float:
    if y < 0:
        return 0.0
    return nCk(r + y - 1, y) * (p ** r) * ((1 - p) ** y)


def mean_negbin_failures(r: int, p: float) -> float:
    return r * (1 - p) / p


def var_negbin_failures(r: int, p: float) -> float:
    return r * (1 - p) / (p * p)
