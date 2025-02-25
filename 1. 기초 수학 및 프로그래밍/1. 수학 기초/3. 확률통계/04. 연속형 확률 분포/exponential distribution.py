import matplotlib.pyplot as plt


def seq(start, stop, step):
    res = []
    current = start
    while current < stop:
        res.append(current)
        current += step
    return res


e = 2.7182818284
beta = 2

x_list = seq(0, beta * 10, 0.01)
p_list = []

for x in x_list:
    prob = (1 / beta) * (e ** ((-1 / beta) * x))
    p_list.append(prob)

plt.plot(x_list, p_list)
plt.show()