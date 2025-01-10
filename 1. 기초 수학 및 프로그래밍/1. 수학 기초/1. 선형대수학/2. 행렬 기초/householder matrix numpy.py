import numpy as np

v = np.array([1, 0, 2, 3])

n = len(v)
outer_mat = np.outer(v, v)
inner_val = np.inner(v, v)
I = np.identity(n)

H = I - (2 / inner_val) * outer_mat