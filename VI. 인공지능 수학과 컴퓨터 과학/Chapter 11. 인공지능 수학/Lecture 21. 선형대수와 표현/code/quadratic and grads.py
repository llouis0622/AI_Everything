import numpy as np


def is_symmetric(A, tol=1e-12):
    A = np.asarray(A)
    return bool(np.allclose(A, A.T, atol=tol, rtol=0))


def quadratic_form(x, W):
    x = np.asarray(x, dtype=float).reshape(-1)
    W = np.asarray(W, dtype=float)
    return float(x @ W @ x)


def is_pos_def(W, tol=1e-12):
    W = np.asarray(W, dtype=float)
    if not is_symmetric(W, tol=tol):
        return False
    eigvals = np.linalg.eigvalsh(W)
    return bool(np.all(eigvals > tol))


def grad_wTx(X, w):
    X = np.asarray(X, dtype=float)
    w = np.asarray(w, dtype=float).reshape(-1)
    return X.T @ (X @ w)


def grad_quadratic_sym(A, x):
    A = np.asarray(A, dtype=float)
    x = np.asarray(x, dtype=float).reshape(-1)
    return 2.0 * (A @ x)
