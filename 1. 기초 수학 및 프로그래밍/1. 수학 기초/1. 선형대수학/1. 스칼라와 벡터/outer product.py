# outer product
def outer_product(a, b):
    res = []
    n1 = len(a)
    n2 = len(b)
    for i in range(n1):
        row = []
        for j in range(n2):
            val = a[i] * b[j]
            row.append(val)
        res.append(row)
    return res


a = [1, 2, 3]
b = [4, 5]