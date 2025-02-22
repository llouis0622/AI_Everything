import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom

p = 0.7

x_list = np.arange(1, 10)
p_list = []

for x in x_list:
    prob = geom.pmf(k=x, p=p)
    p_list.append(prob)
print(p_list)

plt.bar(x_list, p_list)
plt.show()