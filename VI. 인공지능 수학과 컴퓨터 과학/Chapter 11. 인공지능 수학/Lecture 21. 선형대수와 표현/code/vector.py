import numpy as np


def dot(u, v):
    u = np.asarray(u)
    v = np.asarray(v)
    return float(u @ v)


def norm(u, ord=2):
    return float(np.linalg.norm(np.asarray(u), ord=ord))


def cosine(u, v, eps=1e-12):
    u = np.asarray(u)
    v = np.asarray(v)
    return float((u @ v) / (np.linalg.norm(u) * np.linalg.norm(v) + eps))


def projection(u, v, eps=1e-12):
    u = np.asarray(u)
    v = np.asarray(v)
    return (u @ v) / ((v @ v) + eps) * v


def orthogonal_component(u, v, eps=1e-12):
    u = np.asarray(u)
    return u - projection(u, v, eps=eps)


def outer(u, v):
    u = np.asarray(u)
    v = np.asarray(v)
    return np.outer(u, v)


def cross(u, v):
    return np.cross(np.asarray(u), np.asarray(v))


def scalar_triple(u, v, w):
    u = np.asarray(u)
    v = np.asarray(v)
    w = np.asarray(w)
    return float(u @ np.cross(v, w))


def vector_triple(u, v, w):
    u = np.asarray(u)
    v = np.asarray(v)
    w = np.asarray(w)
    return np.cross(u, np.cross(v, w))
