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


def bernoulli(p=0.5, seed=1234567, size=1):
    u_list = pseudo_sample(seed=seed, size=size)
    x_list = [0, 1]
    pmf = {}
    res = []
    for x in x_list:
        prob = (p ** x) * ((1 - p) ** (1 - x))
        pmf[x] = prob
    for u in u_list:
        cumul_prob = 0
        for X in pmf.keys():
            cumul_prob += pmf[X]
            if cumul_prob > u:
                res.append(X)
                break
    return res


bernoulli(p=0.2, size=10)
samples = bernoulli(p=0.2, size=1000)

plt.hist(samples, bins=2)
plt.show()