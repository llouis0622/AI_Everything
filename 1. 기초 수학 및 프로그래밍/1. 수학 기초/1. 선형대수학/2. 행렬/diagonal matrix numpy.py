import numpy as np

# diagonal matrix
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
D = np.diag(A)

# diagonal element
np.diag(D)

# element to diagonal matrix
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
D = np.diag([1, 3, 4])

# matrix * diagonal matrix
AD = np.matmul(A, D)
DA = np.matmul(D, A)