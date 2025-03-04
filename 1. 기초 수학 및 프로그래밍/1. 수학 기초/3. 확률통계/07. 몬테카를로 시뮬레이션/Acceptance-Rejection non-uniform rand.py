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


e = 2.7182818284
c = 14

y = uniform_cont(low=0, high=10, seed=12345, size=20000)
u = uniform_cont(low=0, high=1, seed=77777, size=20000)
n = len(y)

x_list = []

for i in range(n):
    accept_prob = (e ** (-y[i])) / (c * (1 / 10))
    if u[i] < accept_prob:
        x = y[i]
        x_list.append(x)

len(x_list)

plt.hist(x_list, bins=100)
plt.show()