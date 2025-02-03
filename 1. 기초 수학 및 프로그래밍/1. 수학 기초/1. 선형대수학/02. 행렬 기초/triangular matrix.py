# upper triangular matrix
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


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
u_tri(A)

# lower triangular matrix
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

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l_tri(A)