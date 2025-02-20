def var(x_list):
    n = len(x_list)
    mean_x = mean(x_list)
    ss_x = 0
    for x in x_list:
        ss_x += (x - mean_x) ** 2
    res = ss_x / (n - 1)
    return res


def std(x_list):
    var_x = var(x_list)
    res = var_x ** 0.5
    return res


def mean(x_list):
    n = len(x_list)
    sum_x = 0
    for x in x_list:
        sum_x += x
    res = sum_x / n
    return res


x_list = [2, 4, 6, 1, 5, 7, 9, 8, 3]
var_x = var(x_list)
std_x = std(x_list)
print(var_x)
print(std_x)