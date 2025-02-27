import matplotlib.pyplot as plt


def seq(start, stop, step):
    res = []
    current = start
    while current < stop:
        res.append(current)
        current += step
    return res


def factorial(x):
    x_list = list(range(1, x + 1))
    res = 1
    for val in x_list:
        res *= val
    return res


def combination(n, x):
    res = factorial(n) / (factorial(x) * factorial(n - x))
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


alpha = 10
beta = 10
p = 0.1

n = 38
x = 27

beta_function = gamma(alpha + beta) / (gamma(alpha) * gamma(beta))
prior_prob = beta_function * (p ** (alpha - 1)) * ((1 - p) ** (beta - 1))
likelihood = combination(n, x) * (p ** x) * ((1 - p) ** (n - x))
post_prob = likelihood * prior_prob
print(prior_prob)
print(likelihood)
print(post_prob)

alpha = 10
beta = 10
p_list = seq(0, 1, 0.01)

n = 38
x = 27
post_probs = []

for p in p_list:
    beta_function = gamma(alpha + beta) / (gamma(alpha) * gamma(beta))
    prior_prob = beta_function * (p ** (alpha - 1)) * ((1 - p) ** (beta - 1))
    likelihood = combination(n, x) * (p ** x) * ((1 - p) ** (n - x))
    post_prob = likelihood * prior_prob
    post_probs.append(post_prob)

max_prob = max(post_probs)
max_idx = post_probs.index(max_prob)
max_p = p_list[max_idx]

plt.plot(p_list, post_probs)
plt.vlines(max_p, 0, max_prob, color='red', linestyles='--')
plt.show()

print(max_prob)
print(max_idx)
post_probs[64]
p_list[64]