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


def geometric(p=0.5, seed=1234567, size=1):
    u_list = pseudo_sample(seed=seed, size=size)
    x_list = list(range(1, 100))
    pmf = {}
    res = []
    for x in x_list:
        prob = p * ((1 - p) ** (x - 1))
        pmf[x] = prob
    for u in u_list:
        cumul_prob = 0
        for X in pmf.keys():
            cumul_prob += pmf[X]
            if cumul_prob > u:
                res.append(X)
                break
    return res


geometric(p=0.2, size=10)
samples = geometric(p=0.2, size=1000)

plt.hist(samples, bins=15)
plt.show()