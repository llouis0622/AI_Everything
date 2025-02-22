import numpy as np
import matplotlib.pyplot as plt

x_list = np.random.binomial(n=1, p=0.3, size=10000)
print(x_list)

plt.hist(x_list)
plt.show()