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


A = [[1, 0, 2], [0, 2, 1], [2, 1, 1]]
At = transpose(A)
A == At

AA = A
for i in range(9):
    AA = matmul(AA, A)

A = [[1, 0, 3], [2, 1, 4], [0, 1, 1]]
At = transpose(A)

matmul(A, At)
matmul(At, A)