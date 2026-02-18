import math


def mean(x) -> float:
    return sum(x) / len(x)


def variance(x, ddof: int = 0) -> float:
    m = mean(x)
    return sum((xi - m) ** 2 for xi in x) / (len(x) - ddof)


def covariance(x, y, ddof: int = 0) -> float:
    mx = mean(x)
    my = mean(y)
    return sum((x[i] - mx) * (y[i] - my) for i in range(len(x))) / (len(x) - ddof)


def correlation(x, y, ddof: int = 0) -> float:
    cov = covariance(x, y, ddof=ddof)
    vx = variance(x, ddof=ddof)
    vy = variance(y, ddof=ddof)
    return cov / math.sqrt(vx * vy)


def indicator(value, predicate) -> int:
    return 1 if predicate(value) else 0
