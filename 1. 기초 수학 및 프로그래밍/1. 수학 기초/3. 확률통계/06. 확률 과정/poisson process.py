import numpy as np
import matplotlib.pyplot as plt

np.random.seed(777)

lamb = 1
n = 10
x_list = np.random.poisson(lamb, size=n)
xt_list = []
x_axis = list(range(n))

for t in range(n):
    xt = np.sum(x_list[:t])
    xt_list.append(xt)

plt.step(x_axis, xt_list)
plt.xlim(0)
plt.ylim(0)
plt.show()