import matplotlib.pyplot as plt


def seq(start, stop, step):
    res = []
    current = start
    while current < stop:
        res.append(current)
        current += step
    return res


a, b = 1.0, 5.0

x_list = seq(a, b, 0.01)
print(x_list)

p_list = []
for x in x_list:
    prob = 1 / (b - a)
    p_list.append(prob)

plt.plot(x_list, p_list)
plt.show()