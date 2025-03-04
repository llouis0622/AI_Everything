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


def uniform_disc(low=0, high=1, seed=1234567, size=1):
    s_list = pseudo_sample(seed=seed, size=size)
    res = []
    for s in s_list:
        val = int(low + (high - low) * s)
        res.append(val)
    return res


def normal_pdf(mu, s, x):
    pi = 3.1415926535
    e = 2.7182818284
    res = (1 / (((2 * pi) ** 0.5) * s)) * (e ** (-0.5 * (((x - mu) / s) ** 2)))
    return res


def normal_sample(mu, s, seed=1234567, size=1):
    burn_in = 100
    size = burn_in + size
    u_list = pseudo_sample(seed=seed*2, size=size)
    xt_candidates = uniform_cont(low=mu-3*s, high=mu+3*s, size=size)
    x0 = mu
    xt = x0
    res = []

    for i in range(size):
        xt_candidate = xt_candidates[i]
        pi_y = normal_pdf(mu, s, xt_candidate)
        pi_x = normal_pdf(mu, s, xt)
        accept_prob = pi_y / pi_x
        if u_list[i] < accept_prob:
            xt = xt_candidate
        res.append(xt)
    res = res[burn_in:]
    return res


samples = normal_sample(mu=10, s=3, size=1000)

plt.hist(samples, bins=20)
plt.show()