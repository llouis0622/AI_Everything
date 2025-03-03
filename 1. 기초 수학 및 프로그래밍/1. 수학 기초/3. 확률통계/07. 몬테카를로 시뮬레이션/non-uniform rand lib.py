import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2022)

x = np.random.exponential(scale=1, size=1500)

plt.hist(x, bins=100)
plt.show()