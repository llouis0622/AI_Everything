import matplotlib.pyplot as plt


def factorial(x):
    x_list = list(range(1, x + 1))
    res = 1
    for val in x_list:
        res *= val
    return res


def combination(n, x):
    res = factorial(n) / (factorial(x) * factorial(n - x))
    return res


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


def binomial(n, p=0.5, seed=1234567, size=1):
    u_list = pseudo_sample(seed=seed, size=size)
    x_list = list(range(n))
    pmf = {}
    res = []
    for x in x_list:
        prob = combination(n, x) * (p ** x) * ((1 - p) ** (n - x))
        pmf[x] = prob
    for u in u_list:
        cumul_prob = 0
        for X in pmf.keys():
            cumul_prob += pmf[X]
            if cumul_prob > u:
                res.append(X)
                break
    return res


binomial(n=10, p=0.3, size=10)
samples = bin(n=10, p=0.3, size=1000)

plt.hist(samples, bins=8)
plt.show()