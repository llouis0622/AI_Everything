# householder matrix
def householder(v):
    n = len(v)
    outer_mat = outer_product(v, v)
    inner_val = inner_product(v, v)
    V = []
    for i in range(n):
        row = []
        for j in range(n):
            val = (2 / inner_val) * outer_mat[i][j]
            row.append(val)
        V.append(row)
    H = subtract(identity(n), V)
    return H


# outer product
def outer_product(a, b):
    res = []
    n1 = len(a)
    n2 = len(b)
    for i in range(n1):
        row = []
        for j in range(n2):
            val = a[i] * b[j]
            row.append(val)
        res.append(row)
    return res


# inner product
def inner_product(a, b):
    n = len(a)
    res = 0
    for i in range(n):
        res += a[i] * b[i]
    return res


# identity matrix
def identity(n):
    I = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        I.append(row)
    return I


# matrix subtract
def subtract(A, B):
    n = len(A)
    p = len(A[0])
    res = []
    for i in range(n):
        row = []
        for j in range(p):
            val = A[i][j] - B[i][j]
            row.append(val)
        res.append(row)
    return res


a = [1, 0, 2, 3]
householder(a)