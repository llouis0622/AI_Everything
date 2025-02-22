import numpy as np
import matplotlib.pyplot as plt

x_list = np.random.negative_binomial(n=5, p=0.6, size=10000)
print(x_list)

plt.hist(x_list)
plt.show()