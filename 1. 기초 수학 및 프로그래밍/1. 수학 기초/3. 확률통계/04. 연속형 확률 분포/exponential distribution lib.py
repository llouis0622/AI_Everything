import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

beta = 2

x_list = np.arange(0, beta * 10, 0.01)
p_list = []

for x in x_list:
    prob = expon.pdf(x, scale=beta)
    p_list.append(prob)

plt.plot(x_list, p_list)
plt.show()