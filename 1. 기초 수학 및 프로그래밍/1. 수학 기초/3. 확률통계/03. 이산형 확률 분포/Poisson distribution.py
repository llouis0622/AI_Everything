import matplotlib.pyplot as plt


def factorial(x):
    x_list = list(range(1, x + 1))
    res = 1
    for val in x_list:
        res *= val
    return res


e = 2.7182817284

lamb = 2
x_list = list(range(10))
p_list = []

for x in x_list:
    prob = ((e ** (-lamb)) * (lamb ** x)) / factorial(x)
    p_list.append(prob)
print(p_list)

plt.bar(x_list, p_list)
plt.show()