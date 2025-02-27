import numpy as np

x_list = np.random.binomial(n=1, p=0.2, size=10000)
print(x_list)


def moment(x_list, k):
    n = len(x_list)
    sum_xk = 0
    for x in x_list:
        sum_xk += x ** k
    res = sum_xk / n
    return res


moment1 = moment(x_list, 1)
print(moment1)

moment2 = moment(x_list, 2)
print(moment2)

print(moment2 - moment1 ** 2)

x_list = np.random.gamma(shape=3, scale=2, size=10000)
print(x_list)

moment3 = moment(x_list, 1)
print(moment3)

moment4 = moment(x_list, 2)
print(moment4)

alpha_hat = (moment3 ** 2) / (moment4 - moment3 ** 2)
print(alpha_hat)

beta_hat = (moment4 - moment3 ** 2) / moment3
print(beta_hat)