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


n = 38
x = 27
p = 0.1

prob = combination(n, x) * (p ** x) * ((1 - p) ** (n - x))
print(prob)

n = 38
x = 27
p = 0.7

prob = combination(n, x) * (p ** x) * ((1 - p) ** (n - x))
print(prob)

n = 38
x = 27
p_list = seq(0, 1, 0.01)
probs = []

for p in p_list:
    prob = combination(n, x) * (p ** x) * ((1 - p) ** (n - x))
    probs.append(prob)

plt.plot(p_list, probs)
plt.show()

max(probs)
probs.index(max(probs))
probs[71]
p_list[71]