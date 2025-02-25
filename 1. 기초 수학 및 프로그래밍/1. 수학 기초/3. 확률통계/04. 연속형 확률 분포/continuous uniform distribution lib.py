import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

a, b = 1, 5

x_list = np.arange(a, b, 0.01)
p_list = []

for x in x_list:
    prob = uniform.pdf(x, loc=a, scale=b-a)
    p_list.append(prob)

plt.plot(x_list, p_list)
plt.show()