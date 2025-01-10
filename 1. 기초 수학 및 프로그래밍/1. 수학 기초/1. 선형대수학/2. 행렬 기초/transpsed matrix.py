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


A = [[1, 5], [3, 4], [6, 2]]
transpose(A)