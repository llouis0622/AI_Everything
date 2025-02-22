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


n = 10
p = 0.3

x_list = list(range(n + 1))
p_list = []

for x in x_list:
    prob = combination(n, x) * (p ** x) * ((1 - p) ** (n - x))
    p_list.append(prob)
print(p_list)

plt.bar(x_list, p_list)
plt.show()