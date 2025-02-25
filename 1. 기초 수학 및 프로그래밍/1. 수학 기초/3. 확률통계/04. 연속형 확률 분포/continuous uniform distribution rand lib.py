import numpy as np
import matplotlib.pyplot as plt

x_list = np.random.uniform(low=1.0, high=5.0, size=10000)
print(x_list)

plt.hist(x_list)
plt.show()