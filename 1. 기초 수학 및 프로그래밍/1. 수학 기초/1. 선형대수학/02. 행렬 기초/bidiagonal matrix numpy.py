import numpy as np

# upper bidiagonal matrix
A = np.array([[1, 2, 1, 3], [5, 3, 4, 1], [2, 1, 7, 9], [2, 8, 1, 3]])
diag_ele = np.diag(A)
np.diag(diag_ele)
u_diag_ele = np.diag(A, k=1)
np.diag(u_diag_ele, k=1)
u_diag = np.diag(diag_ele) + np.diag(u_diag_ele, k=1)

# lower bidiagonal matrix
A = np.array([[1, 2, 1, 3], [5, 3, 4, 1], [2, 1, 7, 9], [2, 8, 1, 3]])
diag_ele = np.diag(A)
np.diag(diag_ele)
l_diag_ele = np.diag(A, k=-1)
np.diag(u_diag_ele, k=-1)
l_diag = np.diag(diag_ele) + np.diag(u_diag_ele, k=-1)