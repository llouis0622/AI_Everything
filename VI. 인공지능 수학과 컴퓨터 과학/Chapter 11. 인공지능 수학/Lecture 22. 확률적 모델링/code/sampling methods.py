import math
import random


def inverse_cdf_exponential(u: float, beta: float) -> float:
    return -beta * math.log(1 - u)


def discrete_cdf(pmf):
    c = []
    s = 0.0
    for p in pmf:
        s += p
        c.append(s)
    return c


def normalize(weights):
    s = sum(weights)
    return [w / s for w in weights]


def inverse_cdf_discrete(values, pmf, u: float):
    c = discrete_cdf(normalize(pmf))
    lo, hi = 0, len(c) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if u <= c[mid]:
            hi = mid
        else:
            lo = mid + 1
    return values[lo]


def acceptance_rejection(target_pdf, proposal_sample, proposal_pdf, c: float):
    while True:
        y = proposal_sample()
        u = random.random()
        if u <= target_pdf(y) / (c * proposal_pdf(y)):
            return y
