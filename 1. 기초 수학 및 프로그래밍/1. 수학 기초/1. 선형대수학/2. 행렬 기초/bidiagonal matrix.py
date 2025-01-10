# upper bidiagonal matrix
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


A = [[1, 2, 1, 3], [5, 3, 4, 1], [2, 1, 7, 9], [2, 8, 1, 3]]
u_bidiag(A)

# lower bidiagonal matrix
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


A = [[1, 2, 1, 3], [5, 3, 4, 1], [2, 1, 7, 9], [2, 8, 1, 3]]
l_bidiag(A)