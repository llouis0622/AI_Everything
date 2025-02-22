import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 10
p = 0.3

x_list = list(range(n + 1))
p_list = []

for x in x_list:
    prob = binom.pmf(k=x, n=n, p=p)
    p_list.append(prob)
print(p_list)

plt.bar(x_list, p_list)
plt.show()