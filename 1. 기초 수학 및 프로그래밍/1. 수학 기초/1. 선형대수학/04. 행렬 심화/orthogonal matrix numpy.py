import numpy as np

A = np.array([[1 / (2 ** 0.5), -1 / (2 ** 0.5)], [1 / (2 ** 0.5), 1 / (2 ** 0.5)]])
At = np.transpose(A)
res = np.matmul(At, A)