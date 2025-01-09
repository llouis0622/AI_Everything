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


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diag(A)

# diagonal element
def diag_ele(A):
    n = len(A)
    d = []
    for i in range(n):
        d.append(A[i][i])
    return d


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diag_ele(A)

# element to diagonal matrix
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

a = [1, 9, 5]
ele2diag(a)

# matrix mul
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


# matrix * diagonal matrix
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
D = ele2diag([2, 1, 1])
AD = matmul(A, D)
DA = matmul(D, A)