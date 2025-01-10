import numpy as np

# identity matrix
I = np.identity(5)

# matrix * identity matrix
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
I = np.identity(3)
AI = np.matmul(A, I)
IA = np.matmul(I, A)