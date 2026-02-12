import numpy as np


def as_col(x):
    x = np.asarray(x)
    return x.reshape(-1, 1)


def as_row(x):
    x = np.asarray(x)
    return x.reshape(1, -1)


def eye(n, dtype=float):
    return np.eye(n, dtype=dtype)


def zeros(shape, dtype=float):
    return np.zeros(shape, dtype=dtype)


def diag(v):
    v = np.asarray(v)
    return np.diag(v)
