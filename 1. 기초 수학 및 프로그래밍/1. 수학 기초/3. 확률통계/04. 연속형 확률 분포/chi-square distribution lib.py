import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

p = 3

x_list = np.arange(0, p * 5, 0.01)
p_list = []

for x in x_list:
    prob = chi2.pdf(x, df=p)
    p_list.append(prob)


plt.plot(x_list, p_list)
plt.show()