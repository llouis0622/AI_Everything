# singular value decomposition
def svd(A):
    At = transpose(A)
    AtA = matmul(At, A)
    E, V = eig_qr(AtA)
    n = len(AtA)
    for i in range(n):
        E[i][i] = E[i][i] ** 0.5
    S = diag(E)
    Vt = transpose(V)
    AV = matmul(A, V)
    AVt = transpose(AV)
    Ut = []
    for vector in AVt:
        Ut.append(normalize(vector))
    U = transpose(Ut)
    return U, S, Vt


# eigenvalue & eigenvector
def eig_qr(A):
    n = len(A)
    E = deepcopy(A)
    V = identity(n)
    for i in range(30):
        Q, R = qr_gram(E)
        E = matmul(R, Q)
        V = matmul(V, Q)
    return E, V

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


# deepcopy
def deepcopy(A):
    if type(A[0]) == list:
        n = len(A)
        p = len(A[0])
        res = zero_mat(n, p)
        for i in range(0, n):
            for j in range(0, p):
                res[i][j] = A[i][j]
        return res
    else:
        n = len(A)
        res = []
        for i in range(0, n):
            res.append(A[i])
        return res


# identity vector
def identity(n):
    I = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        I.append(row)
    return I


# vector matmul
def matmul(A, B):
    n = len(A)
    p1 = len(A[0])
    p2 = len(B[0])
    res = []
    for i in range(0, n):
        row = []
        for j in range(0, p2):
            val = 0
            for k in range(0, p1):
                val += A[i][k] * B[k][j]
            row.append(val)
        res.append(row)
    return res


# zero_mat
def zero_mat(n, p):
    Z = []
    for i in range(0, n):
        row = []
        for j in range(0, p):
            row.append(0)
        Z.append(row)
    return Z


# diagonal matrix
def diag(A):
    n = len(A)
    D = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(A[i][j])
            else:
                row.append(0)
        D.append(row)
    return D


B = [[3, 6], [2, 3], [1, 2], [5, 5]]
U, S, Vt = svd(B)
matmul(matmul(U, S), Vt)