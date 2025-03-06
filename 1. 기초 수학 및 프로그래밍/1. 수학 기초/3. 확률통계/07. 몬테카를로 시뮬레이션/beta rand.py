import matplotlib.pyplot as plt


def pseudo_sample(x0=16809, mod=(2**31)-1, seed=1234567, size=1):
    res = []
    x = (seed * x0 + 1) % mod
    u = x / mod
    res.append(u)
    for i in range(1, size):
        x = (seed * x + 1) % mod
        u = x / mod
        res.append(u)
    return res


def uniform_cont(low=0, high=1, seed=1234567, size=1):
    s_list = pseudo_sample(seed=seed, size=size)
    res = []
    for s in s_list:
        val = low + (high - low) * s
        res.append(val)
    return res


def seq(start, stop, step):
    res = []
    current = start
    while current < stop:
        res.append(current)
        current += step
    return res


def gamma_function(alpha, x):
    e = 2.7182817284
    res = (x ** (alpha - 1)) * (e ** (-x))
    return res


def gamma(alpha):
    a, b = 0, 100
    x_list = seq(0.0001, 100, 0.001)
    gamma_list = []
    for x in x_list:
        y = gamma_function(alpha, x)
        gamma_list.append(y)
    res = ((b - a) / len(x_list)) * sum(gamma_list)
    return res


def beta_pdf(alpha, beta, x):
    beta_function = ((gamma(alpha + beta)) / (gamma(alpha) * gamma(beta)))
    res = beta_function * (x ** (alpha - 1)) * ((1 - x) ** (beta - 1))
    return res


def beta_sample(alpha, beta, seed=1234567, size=1):
    burn_in = 100
    size = burn_in + size
    u_list = pseudo_sample(seed=seed * 2, size=size)
    xt_candidates = uniform_cont(low=0, high=1, size=size)
    x0 = 0.5
    xt = x0
    res = []

    for i in range(size):
        xt_candidate = xt_candidates[i]
        pi_y = beta_pdf(alpha, beta, xt_candidate)
        pi_x = beta_pdf(alpha, beta, xt)
        accept_prob = pi_y / pi_x
        if u_list[i] < accept_prob:
            xt = xt_candidate
        res.append(xt)
    res = res[burn_in:]
    return res


samples = beta_sample(alpha=0.5, beta=0.5, size=1000)

plt.hist(samples, bins=20)
plt.show()