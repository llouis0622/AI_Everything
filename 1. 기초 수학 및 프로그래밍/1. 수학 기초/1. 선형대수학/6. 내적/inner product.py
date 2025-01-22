# inner product
def inner_product(a, b):
    n = len(a)
    res = 0
    for i in range(n):
        res += a[i] * b[i]
    return res


a = [1, 2, 3]
b = [4, 5, 6]
inner_product(a, b)