import numpy as np

X = np.array([[3, 1, 2], [2, 6, -1], [4, 0, -1]])
y = np.array([[5], [1], [3]])
sol = np.linalg.solve(X, y)