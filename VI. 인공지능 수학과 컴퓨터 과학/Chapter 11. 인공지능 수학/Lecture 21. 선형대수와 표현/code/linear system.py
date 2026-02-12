import numpy as np


def solve_system(A, b):
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    return np.linalg.solve(A, b)


def least_squares(X, y):
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    w, *_ = np.linalg.lstsq(X, y, rcond=None)
    return w


def rref(M, tol=1e-12):
    A = np.asarray(M, dtype=float).copy()
    m, n = A.shape
    r = 0
    pivots = []
    for c in range(n):
        if r >= m:
            break
        pivot = r + np.argmax(np.abs(A[r:, c]))
        if abs(A[pivot, c]) <= tol:
            continue
        if pivot != r:
            A[[r, pivot]] = A[[pivot, r]]
        A[r] = A[r] / A[r, c]
        for i in range(m):
            if i != r:
                A[i] = A[i] - A[i, c] * A[r]
        pivots.append((r, c))
        r += 1
    A[np.abs(A) < tol] = 0.0
    return A, pivots


def nullspace(A, tol=1e-12):
    A = np.asarray(A, dtype=float)
    U, S, Vt = np.linalg.svd(A)
    r = np.sum(S > tol)
    return Vt[r:].T
