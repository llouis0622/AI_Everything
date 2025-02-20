def mean(x_list):
    n = len(x_list)
    sum_x = 0
    for x in x_list:
        sum_x += x
    res = sum_x / n
    return res


x_list = [2, 4, 6, 1, 5, 7, 9, 8, 3]
res = mean(x_list)
print(res)