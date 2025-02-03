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


A = [[1, 3, 1, 4], [3, 9, 5, 15], [0, 2, 1, 1], [0, 4, 2, 3]]
det_rec(A)

B = [[6, 3], [5, 4]]
det_rec(B)


# determinant triangle matrix
def det_tri(A):
    n = len(A)
    X = deepcopy(A)
    n_row_change = 0
    for i in range(n):
        if X[i][i] == 0:
            tmp = X[i + 1]
            X[i + 1] = X[i]
            X[i] = tmp
            n_row_change += 1
        for j in range(i + 1, n):
            ratio = X[j][i] / X[i][i]
            for k in range(n):
                X[j][k] -= ratio * X[i][k]
    n_row_change = (-1) ** (n_row_change)
    res = 1
    for i in range(n):
        res *= X[i][i]
    res *= n_row_change
    return res


A = [[1, 3, 1, 4], [3, 9, 5, 15], [0, 2, 1, 1], [0, 4, 2, 3]]
det_tri(A)

B = [[6, 3], [5, 4]]
det_tri(B)