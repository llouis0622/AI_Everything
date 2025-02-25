import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu = 75
s = 3

x_list = np.arange(mu - 3 * s, mu + 3 * s, 0.01)
p_list = []

for x in x_list:
    prob = norm.pdf(x, loc=mu, scale=s)
    p_list.append(prob)

plt.plot(x_list, p_list)
plt.show()