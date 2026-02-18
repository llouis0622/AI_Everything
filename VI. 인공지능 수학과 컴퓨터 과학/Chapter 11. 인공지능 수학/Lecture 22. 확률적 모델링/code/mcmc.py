import random


def mh_sampler(pi_unnorm, q_sample, q_pdf, x0: float, n: int):
    x = x0
    chain = [x]
    for _ in range(n):
        y = q_sample(x)
        num = pi_unnorm(y) * q_pdf(y, x)
        den = pi_unnorm(x) * q_pdf(x, y)
        a = 1.0 if den <= 0 else min(1.0, num / den)
        if random.random() < a:
            x = y
        chain.append(x)
    return chain
