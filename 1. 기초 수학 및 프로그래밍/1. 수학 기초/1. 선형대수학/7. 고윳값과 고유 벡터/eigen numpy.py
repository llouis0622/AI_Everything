import numpy as np

A = np.array([[3, 0], [8, -1]])
e, v = np.linalg.eig(A)

B = np.array([[4, 0, 1], [-2, 1, 0], [-2, 0, 1]])
e, v = np.linalg.eig(B)