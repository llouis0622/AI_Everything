import math


def pdf_uniform(a: float, b: float):
    c = 1.0 / (b - a)

    def f(x: float) -> float:
        return c if a <= x <= b else 0.0

    return f


def mean_uniform(a: float, b: float) -> float:
    return (a + b) / 2.0


def var_uniform(a: float, b: float) -> float:
    return ((b - a) ** 2) / 12.0


def normal_pdf(x: float, mu: float = 0.0, sigma: float = 1.0) -> float:
    z = (x - mu) / sigma
    return math.exp(-0.5 * z * z) / (math.sqrt(2 * math.pi) * sigma)


def standard_normal_pdf(x: float) -> float:
    return normal_pdf(x, 0.0, 1.0)


def gamma_fn(a: float) -> float:
    return math.gamma(a)


def beta_fn(a: float, b: float) -> float:
    return math.gamma(a) * math.gamma(b) / math.gamma(a + b)


def gamma_pdf(x: float, alpha: float, beta: float) -> float:
    if x <= 0:
        return 0.0
    return (x ** (alpha - 1)) * math.exp(-x / beta) / (gamma_fn(alpha) * (beta ** alpha))


def mean_gamma(alpha: float, beta: float) -> float:
    return alpha * beta


def var_gamma(alpha: float, beta: float) -> float:
    return alpha * (beta ** 2)


def mgf_gamma(t: float, alpha: float, beta: float) -> float:
    return (1 - beta * t) ** (-alpha)


def exponential_pdf(x: float, beta: float) -> float:
    if x < 0:
        return 0.0
    return (1.0 / beta) * math.exp(-x / beta)


def mean_exponential(beta: float) -> float:
    return beta


def var_exponential(beta: float) -> float:
    return beta * beta


def mgf_exponential(t: float, beta: float) -> float:
    return (1 - beta * t) ** (-1.0)


def chi_square_pdf(x: float, p: float) -> float:
    if x <= 0:
        return 0.0
    return gamma_pdf(x, p / 2.0, 2.0)


def mean_chi_square(p: float) -> float:
    return p


def var_chi_square(p: float) -> float:
    return 2.0 * p


def beta_pdf(x: float, a: float, b: float) -> float:
    if x <= 0 or x >= 1:
        return 0.0
    return (x ** (a - 1)) * ((1 - x) ** (b - 1)) / beta_fn(a, b)


def mean_beta(a: float, b: float) -> float:
    return a / (a + b)


def var_beta(a: float, b: float) -> float:
    return (a * b) / (((a + b) ** 2) * (a + b + 1))
