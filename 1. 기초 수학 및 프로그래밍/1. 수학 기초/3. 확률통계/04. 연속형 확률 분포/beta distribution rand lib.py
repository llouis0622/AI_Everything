import numpy as np
import matplotlib.pyplot as plt

x_list = np.random.beta(a=0.5, b=0.5, size=10000)
print(x_list)

plt.hist(x_list)
plt.show()