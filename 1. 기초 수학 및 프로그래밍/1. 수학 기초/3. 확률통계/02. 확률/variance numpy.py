import numpy as np

x_list = [2, 4, 6, 1, 5, 7, 9, 8, 3]
var_x = np.var(x_list, ddof=1)
std_x = np.std(x_list, ddof=1)
print(var_x)
print(std_x)

var_x = np.var(x_list)
std_x = np.std(x_list)
print(var_x)
print(std_x)