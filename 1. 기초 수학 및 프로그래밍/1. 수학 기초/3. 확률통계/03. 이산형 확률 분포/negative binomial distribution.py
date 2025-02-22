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


r = 5
p = 0.6

x_list = list(range(r, r + 20))
p_list = []

for x in x_list:
    prob = combination(x - 1, r - 1) * (p ** r) * ((1 - p) ** (x - r))
    p_list.append(prob)
print(p_list)

plt.bar(x_list, p_list)
plt.show()