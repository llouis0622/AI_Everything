import matplotlib.pyplot as plt


def log(x):
    n = 100000000.0
    res = n * ((x ** (1 / n)) - 1)
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


def uniform_cont(low=0, high=1, seed=1234567, size=1):
    s_list = pseudo_sample(seed=seed, size=size)
    res = []
    for s in s_list:
        val = low + (high - low) * s
        res.append(val)
    return res


u_list = uniform_cont(low=0, high=1, size=1000)
x_list = []
for u in u_list:
    x = -log(u)
    x_list.append(x)

plt.hist(x_list, bins=100)
plt.show()