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


identity(5)

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


# matrix * identity matrix
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
I = identity(3)
AI = matmul(A, I)
IA = matmul(I, A)