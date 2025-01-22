import numpy as np

A = np.array([[1, 0, 1], [0, 1, 1], [1, 2, 0]])
Q, R = np.linalg.qr(A)