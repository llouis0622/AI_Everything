# zero matrix
def zero_mat(n, p):
    Z = []
    for i in range(n):
        row = []
        for j in range(p):
            row.append(0)
        Z.append(row)
    return Z


zero_mat(3, 2)