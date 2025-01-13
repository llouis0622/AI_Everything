# inverse matrix
def inv(A):
    n = len(A)
    X = deepcopy(A)
    C = []
    for i in range(n):
        row_C = []
        idx_r = list(range(n))
        idx_r.remove(i)
        for j in range(n):
            idx_c = list(range(n))
            idx_c.remove(j)
            M = []
            for k in idx_r:
                row_M = []
                for l in idx_c:
                    val = X[k][l]
                    row_M.append(val)
                M.append(row_M)
            Mij = det_rec(M)
            Cij = ((-1) ** (i + j)) * Mij
            row_C.append(Cij)
        C.append(row_C)
    adj = transpose(C)
    res = scalar_mul(1 / det_rec(X), adj)
    return res


# zero matrix
def zero_mat(n, p):
    Z = []
    for i in range(n):
        row = []
        for j in range(p):
            row.append(0)
        Z.append(row)
    return Z


# deepcopy
def deepcopy(A):
    if type(A[0]) == list:
        n = len(A)
        p = len(A[0])
        res = zero_mat(n, p)
        for i in range(n):
            for j in range(p):
                res[i][j] = A[i][j]
        return res
    else:
        n = len(A)
        res = []
        for i in range(n):
            res.append(A[i])
        return res


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


# matrix scalar mul
def scalar_mul(b, A):
    n = len(A)
    p = len(A[0])
    res = []
    for i in range(n):
        row = []
        for j in range(p):
            val = b * A[i][j]
            row.append(val)
        res.append(row)
    return res


# determinant recursion
def det_rec(A):
    n = len(A)
    res = 0
    if n == 2:
        res = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return res
    for i in range(n):
        X = deepcopy(A)
        X = X[1:]
        nx = len(X)
        for j in range(nx):
            X[j] = X[j][0:i] + X[j][i + 1:]
        sign = (-1) ** (i % 2)
        sub_det = det_rec(X)
        res += sign * A[0][i] * sub_det
    return res


A = [[3, 2, 0], [-1, -3, 6], [2, 3, -5]]
inv(A)