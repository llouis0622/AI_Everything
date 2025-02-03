# matrix sum
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


A = [[2, 7], [3, 4], [6, 1]]
B = [[1, 4], [4, -1], [2, 5]]
add(A, B)

# matrix sub
def sub(A, B):
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


A = [[2, 7], [3, 4], [6, 1]]
B = [[1, 4], [4, -1], [2, 5]]
sub(A, B)

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


A = [[2, 7], [3, 4], [6, 1]]
b = 2
scalar_mul(b, A)

# matrix idx mul
def ele_product(A, B):
    n = len(A)
    p = len(A[0])
    res = []
    for i in range(n):
        row = []
        for j in range(p):
            val = A[i][j] * B[j][i]
            row.append(val)
        res.append(row)
    return res


A = [[1, 5], [6, 4], [2, 7]]
B = [[5, -1], [1, 2], [4, 1]]
ele_product(A, B)

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


A = [[2, 7], [3, 4], [5, 2]]
B = [[3, -3, 5], [-1, 2, -1]]
matmul(A, B)