import matplotlib.pyplot as plt


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


alpha, beta = 0.5, 0.5
e = 2.7182817284

x_list = seq(0.01, 1, 0.01)
p_list = []

beta_function = ((gamma(alpha + beta)) / (gamma(alpha) * gamma(beta)))
for x in x_list:
    prob = beta_function * (x ** (alpha - 1)) * ((1 - x) ** (beta - 1))
    p_list.append(prob)

plt.plot(x_list, p_list)
plt.show()