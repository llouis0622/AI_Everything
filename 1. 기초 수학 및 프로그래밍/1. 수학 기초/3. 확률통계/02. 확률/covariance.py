def cov(x1_list, x2_list):
    n = len(x1_list)
    m1 = mean(x1_list)
    m2 = mean(x2_list)
    sm = 0
    for i in range(n):
        sm += (x1_list[i] - m1) * (x2_list[i] - m2)
    res = sm / (n - 1)
    return res


def corrcoef(x1_list, x2_list):
    covariance = cov(x1_list, x2_list)
    std1 = std(x1_list)
    std2 = std(x2_list)
    res = covariance / (std1 * std2)
    return res


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


x1_list = [2, 4, 6, 1, 5, 7, 9, 8, 3]
x2_list = [3, 1, 2, 7, 3, 8, 3, 4, 5]
covariance = cov(x1_list, x2_list)
corr = corrcoef(x1_list, x2_list)
print(covariance)
print(corr)