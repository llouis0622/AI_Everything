import numpy as np
import matplotlib.pyplot as plt

np.random.seed(777)


def poisson_process(lamb, n):
    x_list = np.random.poisson(lamb, size=n)
    xt_list = []

    for t in range(n):
        xt = np.sum(x_list[:t])
        xt_list.append(xt)
    return xt_list


n = 10
x_axis = list(range(n))

xt_list1 = poisson_process(1, n)
xt_list2 = poisson_process(2, n)
xt_list5 = poisson_process(5, n)

plt.step(x_axis, xt_list1, color='b', label='lamb=1')
plt.step(x_axis, xt_list2, color='r', label='lamb=2')
plt.step(x_axis, xt_list5, color='g', label='lamb=5')
plt.legend()
plt.xlim(0)
plt.ylim(0)
plt.show()