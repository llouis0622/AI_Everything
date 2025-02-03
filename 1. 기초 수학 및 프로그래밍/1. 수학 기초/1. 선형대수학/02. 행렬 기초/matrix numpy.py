import numpy as np

# matrix sum
A = np.array([[2, 7], [3, 4], [6, 1]])
B = np.array([[1, 4], [4, -1], [2, 5]])
C = A + B

# matrix sub
A = np.array([[2, 7], [3, 4], [6, 1]])
B = np.array([[1, 4], [4, -1], [2, 5]])
C = A - B

# matrix scalar mul
A = np.array([[2, 7], [3, 4], [6, 1]])
b = 2
C = b * A

# matrix idx mul
A = np.array([[1, 5], [6, 4], [2, 7]])
B = np.array([[5, -1], [1, 2], [4, 1]])
C = np.multiply(A, B)

# matrix mul
A = np.array([[2, 7], [3, 4], [5, 2]])
B = np.array([[3, -3, 5], [-1, 2, -1]])
C = np.matmul(A, B)