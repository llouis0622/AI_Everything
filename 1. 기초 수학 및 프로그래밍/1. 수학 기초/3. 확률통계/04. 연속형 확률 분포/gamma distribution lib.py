import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

alpha, beta = 2, 1

x_list = np.arange(0, alpha * beta * 5, 0.01)
p_list = []

for x in x_list:
    prob = gamma.pdf(x, a=alpha, scale=beta)
    p_list.append(prob)

plt.plot(x_list, p_list)
plt.show()