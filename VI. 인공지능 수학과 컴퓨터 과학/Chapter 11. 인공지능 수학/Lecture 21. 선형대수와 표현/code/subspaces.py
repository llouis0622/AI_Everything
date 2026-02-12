import numpy as np


def nullspace(A, tol=1e-12):
    A = np.asarray(A, dtype=float)
    U, S, Vt = np.linalg.svd(A)
    r = np.sum(S > tol)
    return Vt[r:].T


def rank(A, tol=1e-12):
    return int(np.linalg.matrix_rank(np.asarray(A, dtype=float), tol=tol))


def nullity(A, tol=1e-12):
    A = np.asarray(A, dtype=float)
    return A.shape[1] - rank(A, tol=tol)


def column_space_basis(A, tol=1e-12):
    A = np.asarray(A, dtype=float)
    Q, R = np.linalg.qr(A)
    diagR = np.abs(np.diag(R)) if R.size else np.array([])
    r = int(np.sum(diagR > tol))
    return Q[:, :r]


def row_space_basis(A, tol=1e-12):
    return column_space_basis(np.asarray(A, dtype=float).T, tol=tol)


def left_nullspace(A, tol=1e-12):
    return nullspace(np.asarray(A, dtype=float).T, tol=tol)
