# vector sum
def v_add(u, v):
    n = len(u)
    w = []
    for i in range(n):
        val = u[i] + v[i]
        w.append(val)
    return w


u = [1, 2, 3]
v = [4, 5, 6]
v_add(u, v)


# vector sub
def v_sub(u, v):
    n = len(u)
    w = []
    for i in range(n):
        val = u[i] - v[i]
        w.append(val)
    return w


u = [7, 3, 9]
v = [2, 5, 7]
v_sub(u, v)


# vector scalar mul
def v_scalar_mul(a, u):
    n = len(u)
    w = []
    for i in range(n):
        val = a * u[i]
        w.append(val)
    return w


u = [2, 4, 3]
a = 3
v_scalar_mul(a, u)


# vector idx mul
def v_idx_mul(u, v):
    n = len(u)
    w = []
    for i in range(n):
        val = u[i] * v[i]
        w.append(val)
    return w


u = [1, 2, 4]
v = [7, 3, 2]
v_idx_mul(u, v)


# vector div
def v_div(u, v):
    n = len(u)
    w = []
    for i in range(n):
        val = u[i] / v[i]
        w.append(val)
    return w


u = [6, 5, 9]
v = [2, 2, -3]
v_div(u, v)