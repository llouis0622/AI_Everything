import numpy as np
from scipy.linalg import lu

A = np.array([[2, -2, -2], [0, -2, 2], [-1, 5, 2]])
P, L, U = lu(A)