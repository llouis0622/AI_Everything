def zero_mat(n, p):
    Z = []
    for i in range(n):
        row = []
        for j in range(p):
            row.append(0)
        Z.append(row)
    return Z


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


def v_add(u, v):
    n = len(u)
    w = []
    for i in range(n):
        val = u[i] + v[i]
        w.append(val)
    return w


def v_subtract(u, v):
    n = len(u)
    w = []
    for i in range(n):
        val = u[i] - v[i]
        w.append(val)
    return w


def scalar_v_mul(a, u):
    n = len(u)
    w = []
    for i in range(n):
        val = a * u[i]
        w.append(val)
    return w


def v_mul(u, v):
    n = len(u)
    w = []
    for i in range(n):
        val = u[i] * v[i]
        w.append(val)
    return w


def v_div(u, v):
    n = len(u)
    w = []
    for i in range(n):
        val = u[i] / v[i]
        w.append(val)
    return w


def add(A, B):
    n = len(A)
    p = len(A[0])
    res = []
    for i in range(n):
        row = []
        for j in range(p):
            val = A[i][j] + B[i][j]
            row.append(val)
        res.append(row)
    return res


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


def ele_product(A, B):
    n = len(A)
    p = len(A[0])
    res = []
    for i in range(n):
        row = []
        for j in range(p):
            val = A[i][j] * B[i][j]
            row.append(val)
        res.append(row)
    return res


def matmul(A, B):
    n = len(A)
    p1 = len(A[0])
    p2 = len(B[0])
    res = []
    for i in range(n):
        row = []
        for j in range(p2):
            val = 0
            for k in range(p1):
                val += A[i][k] * B[k][j]
            row.append(val)
        res.append(row)
    return res


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


def diag_ele(A):
    n = len(A)
    d = []
    for i in range(n):
        d.append(A[i][i])
    return d


def ele2diag(a):
    n = len(a)
    D = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(a[i])
            else:
                row.append(0)
        D.append(row)
    return D


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


def u_tri(A):
    n = len(A)
    p = len(A[0])
    utri = []
    for i in range(n):
        row = []
        for j in range(p):
            if i > j:
                row.append(0)
            else:
                row.append(A[i][j])
        utri.append(row)
    return utri


def l_tri(A):
    n = len(A)
    p = len(A[0])
    ltri = []
    for i in range(n):
        row = []
        for j in range(p):
            if i < j:
                row.append(0)
            else:
                row.append(A[i][j])
        ltri.append(row)
    return ltri


def toeplitz(a, b):
    n1 = len(a)
    n2 = len(b)
    A = []
    for i in range(n1):
        row = []
        for j in range(n2):
            if i > j:
                row.append(a[i - j])
            else:
                row.append(b[j - i])
        A.append(row)
    return A


def u_bidiag(A):
    n = len(A)
    p = len(A[0])
    res = []
    for i in range(n):
        row = []
        for j in range(p):
            if i > j or j - i > 1:
                row.append(0)
            else:
                row.append(A[i][j])
        res.append(row)
    return res


def l_bidiag(A):
    n = len(A)
    p = len(A[0])
    res = []
    for i in range(n):
        row = []
        for j in range(p):
            if i < j or i - j > 1:
                row.append(0)
            else:
                row.append(A[i][j])
        res.append(row)
    return res


def inner_product(a, b):
    n = len(a)
    res = 0
    for i in range(n):
        res += a[i] * b[i]
    return res


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


def solve(A, b):
    X = deepcopy(A)
    sol = deepcopy(b)
    n = len(X)
    for i in range(n):
        x_row = X[i]
        y_val = sol[i]
        if x_row[i] != 0:
            tmp = 1 / x_row[i]
        else:
            tmp = 0
        x_row = [element * tmp for element in x_row]
        y_val = y_val * tmp
        X[i] = x_row
        sol[i] = y_val
        for j in range(n):
            if i == j:
                continue
            x_next = X[j]
            y_next = sol[j]
            x_tmp = [element * -x_next[i] for element in x_row]
            y_tmp = y_val * (-x_next[i])
            for k in range(len(x_row)):
                x_next[k] = x_tmp[k] + x_next[k]
            y_next = y_tmp + y_next
            X[j] = x_next
            sol[j] = y_next
    return sol


def norm(a):
    n = len(a)
    res = 0
    for i in range(n):
        res += a[i] ** 2
    res = res ** (0.5)
    return res


def normalize(a):
    n = len(a)
    v = []
    for i in range(n):
        tmp = a[i] / norm(a)
        v.append(tmp)
    return v


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
                X[j][k] = X[j][k] - ratio * X[i][k]
    n_row_change = (-1) ** (n_row_change)
    res = 1
    for i in range(n):
        res *= X[i][i]
    res *= n_row_change
    return res


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


def qr_gram(A):
    n = len(A)
    p = len(A[0])
    At = transpose(A)
    U = []
    norm_list = []
    V = []
    Q = []
    R = []
    for i in range(p):
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
    for i in range(p):
        r = []
        for j in range(p):
            if i > j:
                r.append(0)
            else:
                r_ele = inner_product(At[j], V[i])
                r.append(r_ele)
        R.append(r)
    return Q, R


def sign(a):
    res = 1
    if a < 0:
        res = -1
    return res


def eig_qr(A):
    n = len(A)
    E = deepcopy(A)
    V = identity(n)
    for i in range(30):
        Q, R = qr_gram(E)
        E = matmul(R, Q)
        V = matmul(V, Q)
    return E, V


def qr_householder(A):
    n = len(A)
    p = len(A[0])
    H_list = []
    for i in range(p):
        if i == 0:
            A1 = deepcopy(A)
            exA = A1
        elif i < p - 1:
            Ai = []
            for j in range(1, len(exA)):
                row = []
                for k in range(1, len(exA[0])):
                    row.append(HA[j][k])
                Ai.append(row)
            exA = Ai
        elif i == p - 1:
            Ap = []
            for j in range(1, len(HA)):
                Ap.append(HA[j][1])
            exA = Ap
        if i < p - 1:
            a = transpose(exA)[0]
        else:
            a = exA
        nm = norm(a)
        e = [1]
        for j in range(len(a) - 1):
            e.append(0)
        tmp_e = []
        for j in range(len(e)):
            val = sign(a[0]) * nm * e[j]
            tmp_e.append(val)
        v = v_add(a, tmp_e)
        H = householder(v)
        if i == p - 1:
            HA = []
            for j in range(len(H)):
                val = 0
                for k in range(len(H[0])):
                    val += H[j][k] * exA[k]
                HA.append(val)
        else:
            HA = matmul(H, exA)
        H_list.append(H)
        if i > 0:
            tmp_H = identity(len(A))
            for j in range(i, len(A)):
                for k in range(i, len(A)):
                    tmp_H[j][k] = H_list[-1][j - i][k - i]
            H_list[-1] = tmp_H
    Q = deepcopy(H_list[0])
    for j in range(len(H_list) - 1):
        Q = matmul(Q, H_list[j + 1])
    R = deepcopy(H_list[-1])
    for j in range(1, len(H_list)):
        R = matmul(R, H_list[-(j + 1)])
    R = matmul(R, A)
    return Q, R


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


def lu_decomp(A):
    n = len(A)
    p = len(A[0])
    L = [[0] * p for i in range(n)]
    U = []
    for i in range(n):
        a = A[i]
        val = 1 / a[i]
        L[i][i] = 1 / val
        a = [element * val for element in a]
        U.append(a)
        for j in range(i + 1, n):
            row = A[j]
            a_tmp = [element * -row[i] for element in a]
            L[j][i] = row[i]
            A[j] = [a_tmp[k] + row[k] for k in range(p)]
    return L, U