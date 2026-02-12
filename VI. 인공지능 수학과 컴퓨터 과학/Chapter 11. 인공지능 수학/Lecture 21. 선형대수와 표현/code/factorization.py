import numpy as np


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


def gram_schmidt(S, tol=1e-12):
    S = np.asarray(S, dtype=float)
    m, n = S.shape
    U = np.zeros((m, n), dtype=float)
    k = 0
    for j in range(n):
        v = S[:, j].copy()
        for i in range(k):
            v -= (U[:, i] @ S[:, j]) / (U[:, i] @ U[:, i]) * U[:, i]
        if np.linalg.norm(v) > tol:
            U[:, k] = v
            k += 1
    return U[:, :k]


def qr(A):
    return np.linalg.qr(np.asarray(A, dtype=float))


def qr_householder(A):
    A = np.asarray(A, dtype=float).copy()
    m, n = A.shape
    Q = np.eye(m)
    R = A.copy()
    for k in range(min(m, n)):
        x = R[k:, k]
        Hk = householder(x)
        H = np.eye(m)
        H[k:, k:] = Hk
        R = H @ R
        Q = Q @ H.T
    return Q, R


def lu(A):
    A = np.asarray(A, dtype=float)
    n = A.shape[0]
    L = np.eye(n)
    U = A.copy()
    for k in range(n - 1):
        pivot = U[k, k]
        for i in range(k + 1, n):
            if pivot == 0.0:
                continue
            L[i, k] = U[i, k] / pivot
            U[i, k:] = U[i, k:] - L[i, k] * U[k, k:]
    return L, U


def solve_lu(A, b):
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    L, U = lu(A)

    y = np.zeros_like(b, dtype=float)
    for i in range(L.shape[0]):
        y[i] = b[i] - L[i, :i] @ y[:i]

    x = np.zeros_like(b, dtype=float)
    for i in range(U.shape[0] - 1, -1, -1):
        x[i] = (y[i] - U[i, i + 1:] @ x[i + 1:]) / U[i, i]
    return x


def eig(A):
    A = np.asarray(A, dtype=float)
    w, V = np.linalg.eig(A)
    return w, V


def eigh_symmetric(A):
    A = np.asarray(A, dtype=float)
    w, Q = np.linalg.eigh(A)
    return w, Q


def diagonalize(A, tol=1e-10):
    w, V = np.linalg.eig(np.asarray(A, dtype=float))
    if np.linalg.matrix_rank(V, tol=tol) < V.shape[0]:
        return None
    D = np.diag(w)
    Pinv = np.linalg.inv(V)
    return V, D, Pinv


def svd(A):
    A = np.asarray(A, dtype=float)
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    return U, S, Vt


def low_rank_approx(A, k):
    U, S, Vt = svd(A)
    return U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
