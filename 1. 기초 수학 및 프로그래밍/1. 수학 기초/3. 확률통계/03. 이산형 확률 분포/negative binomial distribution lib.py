import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nbinom

r = 5
p = 0.6

x_list = np.arange(r, r + 20)
p_list = []

for x in x_list:
    prob = nbinom.pmf(k=x, n=r, p=p)
    p_list.append(prob)
print(p_list)

plt.bar(x_list, p_list)
plt.show()