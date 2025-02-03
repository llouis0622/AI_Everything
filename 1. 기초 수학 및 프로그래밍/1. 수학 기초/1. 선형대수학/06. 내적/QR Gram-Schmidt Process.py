# Gram-Schmidt Process
def qr_gram(A):
    n = len(A)
    p = len(A[0])
    At = transpose(A)
    U = []
    norm_list = []
    V = []
    Q = []
    R = []
    for i in range(n):
        if i == 0:
            u = At[i]
            norm_u = norm(u)
            U.append(u)
            norm_list.append(norm_u)
        else:
            a = At[i]
            dp_list = []
            for j in range(i):
                dp = inner_product(a, U[j])
                dp_list.append(dp)
            u = []
            for j in range(n):
                val = a[j]
                for k in range(i):
                    val -= (dp_list[k] / norm_list[k] ** 2) * U[k][j]
                u.append(val)
            norm_u = norm(u)
            U.append(u)
            norm_list.append(norm_u)
        v = normalize(u)
        V.append(v)
    Q = transpose(V)
    for i in range(n):
        r = []
        for j in range(n):
            if i > j:
                r.append(0)
            else:
                r_ele = inner_product(At[j], V[i])
                r.append(r_ele)
        R.append(r)
    return Q, R


# transposed matrix
def transpose(A):
    n = len(A)
    p = len(A[0])
    At = []
    for i in range(p):
        row = []
        for j in range(n):
            val = A[j][i]
            row.append(val)
        At.append(row)
    return At


# vector norm
def norm(a):
    n = len(a)
    res = 0
    for i in range(n):
        res += a[i] ** 2
    res = res ** 0.5
    return res


# inner product
def inner_product(a, b):
    n = len(a)
    res = 0
    for i in range(n):
        res += a[i] * b[i]
    return res


# vector normalize
def normalize(a):
    n = len(a)
    v = []
    for i in range(n):
        tmp = a[i] / norm(a)
        v.append(tmp)
    return v


A = [[1, 0, 1], [0, 1, 1], [1, 2, 0]]
Q, R = qr_gram(A)