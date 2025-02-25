import numpy as np
import matplotlib.pyplot as plt

x_list = np.random.normal(loc=75, scale=3, size=10000)
print(x_list)

plt.hist(x_list)
plt.show()