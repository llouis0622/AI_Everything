import numpy as np

# vector sum
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
w = u + v

# vector sub
u = np.array([7, 3, 9])
v = np.array([2, 5, 7])
w = u - v


# vector scalar mul
a = 3
u = np.array([1, 2, 4])
w = a * u


# vector idx mul
u = np.array([1, 2, 4])
v = np.array([7, 3, 2])
w = u * v


# vector div
u = np.array([6, 5, 9])
v = np.array([2, 2, -3])
w = u / v