import numpy as np

x1_list = [2, 4, 6, 1, 5, 7, 9, 8, 3]
x2_list = [3, 1, 2, 7, 3, 8, 3, 4, 5]

covariance = np.cov(x1_list, x2_list)
print(covariance)

corr = np.corrcoef(x1_list, x2_list)
print(corr)