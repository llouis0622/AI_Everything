import numpy as np

A = np.array([[1, 0, 2], [0, 2, 1], [2, 1, 1]])
At = np.transpose(A)
A == At

AA = A
for i in range(9):
    AA = np.matmul(AA, A)

A = np.array([[1, 0, 3], [2, 1, 4], [0, 1, 1]])
At = np.transpose(A)
np.matmul(A, At)
np.matmul(At, A)