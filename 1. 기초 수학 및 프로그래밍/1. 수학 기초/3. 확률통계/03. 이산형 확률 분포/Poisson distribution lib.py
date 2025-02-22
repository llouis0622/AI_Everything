import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

lamb = 2
x_list = np.arange(10)
p_list = []

for x in x_list:
    prob = poisson.pmf(k=x, mu=lamb)
    p_list.append(prob)
print(p_list)

plt.bar(x_list, p_list)
plt.show()