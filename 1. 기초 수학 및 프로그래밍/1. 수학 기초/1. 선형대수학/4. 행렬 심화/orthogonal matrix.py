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


# orthogonal matrix
A = [[1 / (2 ** 0.5), -1 / (2 ** 0.5)], [1 / (2 ** 0.5), 1 / (2 ** 0.5)]]
At = transpose(A)
res = matmul(At, A)