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


def exponential_pdf(beta, x):
    e = 2.7182818284
    res = (1 / beta) * (e ** ((-1 / beta) * x))
    return res


def exponential_sample(beta, seed=1234567, size=1):
    burn_in = 100
    size = burn_in + size
    u_list = pseudo_sample(seed=seed * 2, size=size)
    xt_candidates = uniform_cont(low=0, high=10 * beta, size=size)
    x0 = beta
    xt = x0
    res = []

    for i in range(size):
        xt_candidate = xt_candidates[i]
        pi_y = exponential_pdf(beta, xt_candidate)
        pi_x = exponential_pdf(beta, xt)
        accept_prob = pi_y / pi_x
        if u_list[i] < accept_prob:
            xt = xt_candidate
        res.append(xt)
    res = res[burn_in:]
    return res


samples = exponential_sample(beta=2, size=1000)

plt.hist(samples, bins=20)
plt.show()