import math
import random


def markov_chain_sample(P, x0: int, n: int):
    k = len(P)
    x = x0
    path = [x]
    for _ in range(n):
        u = random.random()
        s = 0.0
        nx = 0
        for j in range(k):
            s += P[x][j]
            if u <= s:
                nx = j
                break
        x = nx
        path.append(x)
    return path


def poisson_process_counts(lam: float, t: float) -> int:
    L = math.exp(-lam * t)
    k = 0
    p = 1.0
    while p > L:
        k += 1
        p *= random.random()
    return k - 1


def brownian_path(T: float, n: int, sigma: float = 1.0):
    dt = T / n
    x = 0.0
    path = [x]
    for _ in range(n):
        x += random.gauss(0.0, sigma * math.sqrt(dt))
        path.append(x)
    return path


def gbm_path(S0: float, T: float, n: int, mu: float, sigma: float):
    dt = T / n
    S = S0
    path = [S]
    for _ in range(n):
        z = random.gauss(0.0, 1.0)
        S *= math.exp((mu - 0.5 * sigma * sigma) * dt + sigma * math.sqrt(dt) * z)
        path.append(S)
    return path
