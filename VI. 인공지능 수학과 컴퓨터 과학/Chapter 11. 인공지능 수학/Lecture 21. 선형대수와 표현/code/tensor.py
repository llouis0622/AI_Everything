import numpy as np


def tensor_norm(X):
    X = np.asarray(X, dtype=float)
    return float(np.linalg.norm(X.ravel(), ord=2))


def tensor_inner(X, Y):
    X = np.asarray(X, dtype=float)
    Y = np.asarray(Y, dtype=float)
    return float(np.tensordot(X, Y, axes=X.ndim))


def rank_one_tensor(v_list):
    T = np.asarray(v_list[0], dtype=float)
    for v in v_list[1:]:
        T = np.multiply.outer(T, np.asarray(v, dtype=float))
    return T


def unfold(X, mode):
    X = np.asarray(X, dtype=float)
    order = [mode] + [i for i in range(X.ndim) if i != mode]
    Y = np.transpose(X, axes=order)
    return Y.reshape(X.shape[mode], -1)


def n_mode_product(X, U, mode):
    X = np.asarray(X, dtype=float)
    U = np.asarray(U, dtype=float)
    Xn = unfold(X, mode)
    Yn = U @ Xn
    inv_order = np.argsort([mode] + [i for i in range(X.ndim) if i != mode])
    Y = Yn.reshape([U.shape[0]] + [X.shape[i] for i in range(X.ndim) if i != mode])
    return np.transpose(Y, axes=inv_order)


def einsum_inner(X, Y):
    X = np.asarray(X, dtype=float)
    Y = np.asarray(Y, dtype=float)
    return float(np.einsum("...,...->", X, Y))


def einsum_matmul(A, B):
    A = np.asarray(A, dtype=float)
    B = np.asarray(B, dtype=float)
    return np.einsum("ik,kj->ij", A, B)
