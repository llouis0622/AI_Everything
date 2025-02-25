import matplotlib.pyplot as plt


def seq(start, stop, step):
    res = []
    current = start
    while current < stop:
        res.append(current)
        current += step
    return res


pi = 3.1415926535
e = 2.7182818284

mu = 75
s = 3

x_list = seq(mu - 3 * s, mu + 3 * s, 0.01)
p_list = []

for x in x_list:
    prob = (1 / (((2 * pi) ** 0.5) * s)) * (e ** (-0.5 * (((x - mu) / s) ** 2)))
    p_list.append(prob)

plt.plot(x_list, p_list)
plt.show()