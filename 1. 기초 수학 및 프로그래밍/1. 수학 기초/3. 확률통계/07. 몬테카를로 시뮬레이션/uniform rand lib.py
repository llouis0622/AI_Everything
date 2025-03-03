import random
import numpy as np

random.seed(1234567)

random.uniform(1, 2)
random.randint(1, 10)

np.random.seed(1234567)

x_list = np.random.uniform(low=1, high=2, size=5)
print(x_list)

x_list = np.random.randint(low=0, high=1, size=10)
print(x_list)

x_list = np.random.randint(low=0, high=2, size=10)
print(x_list)