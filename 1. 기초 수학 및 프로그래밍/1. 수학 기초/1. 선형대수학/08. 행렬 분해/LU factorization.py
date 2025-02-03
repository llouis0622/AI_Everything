# LU factorization
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


A = [[2, -2, -2], [0, -2, 2], [-1, 5, 2]]
L, U = lu_decomp(A)