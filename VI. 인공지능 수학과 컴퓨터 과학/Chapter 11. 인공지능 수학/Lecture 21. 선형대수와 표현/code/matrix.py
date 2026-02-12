import numpy as np


def is_symmetric(A, tol=1e-12):
    A = np.asarray(A)
    return bool(np.allclose(A, A.T, atol=tol, rtol=0))


def trace(A):
    return float(np.trace(np.asarray(A)))


def hadamard(A, B):
    return np.asarray(A) * np.asarray(B)


def matmul(A, B):
    return np.asarray(A) @ np.asarray(B)


def transpose(A):
    return np.asarray(A).T


def det(A):
    return float(np.linalg.det(np.asarray(A, dtype=float)))


def inv(A):
    return np.linalg.inv(np.asarray(A, dtype=float))


def inv_via_solve(A):
    A = np.asarray(A, dtype=float)
    n = A.shape[0]
    return np.linalg.solve(A, np.eye(n))


def make_diagonal(d):
    d = np.asarray(d, dtype=float)
    D = np.diag(d)
    D_inv = np.diag(1.0 / d)
    return D, D_inv


def is_orthogonal(Q, tol=1e-12):
    Q = np.asarray(Q, dtype=float)
    I = np.eye(Q.shape[0])
    return bool(np.allclose(Q.T @ Q, I, atol=tol, rtol=0))


def similarity_transform(A, P):
    A = np.asarray(A, dtype=float)
    P = np.asarray(P, dtype=float)
    return np.linalg.inv(P) @ A @ P


def kron(A, B):
    return np.kron(np.asarray(A), np.asarray(B))


def toeplitz_matrix(first_col, first_row=None):
    try:
        from scipy.linalg import toeplitz
        c = np.asarray(first_col)
        r = np.asarray(first_row) if first_row is not None else None
        return toeplitz(c, r)
    except Exception:
        c = np.asarray(first_col, dtype=float).reshape(-1)
        if first_row is None:
            r = np.zeros_like(c)
            r[0] = c[0]
        else:
            r = np.asarray(first_row, dtype=float).reshape(-1)
        n = c.shape[0]
        m = r.shape[0]
        T = np.zeros((n, m), dtype=float)
        for i in range(n):
            for j in range(m):
                k = i - j
                if k >= 0:
                    if k < n:
                        T[i, j] = c[k]
                else:
                    kk = -k
                    if kk < m:
                        T[i, j] = r[kk]
        return T


def householder(x):
    x = np.asarray(x, dtype=float).reshape(-1)
    n = x.shape[0]
    e1 = np.zeros(n, dtype=float)
    e1[0] = 1.0
    alpha = np.linalg.norm(x)
    if alpha == 0.0:
        return np.eye(n)
    v = x + np.sign(x[0]) * alpha * e1
    v = v / np.linalg.norm(v)
    return np.eye(n) - 2.0 * np.outer(v, v)
