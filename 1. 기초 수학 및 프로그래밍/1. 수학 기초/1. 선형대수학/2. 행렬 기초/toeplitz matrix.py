# toeplitz matrix
def toeplitz(a, b):
    n1 = len(a)
    n2 = len(b)
    A = []
    for i in range(n1):
        row = []
        for j in range(n2):
            if i > j:
                row.append(a[i-j])
            else:
                row.append(b[j-i])
        A.append(row)
    return A


a = [1, 0, -2, -4]
b = [1, 3, 5, 7, 9]
toeplitz(a, b)