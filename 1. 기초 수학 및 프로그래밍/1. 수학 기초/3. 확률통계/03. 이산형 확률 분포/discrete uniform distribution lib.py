import matplotlib.pyplot as plt
from scipy.stats import randint

a, b = 1, 5

x_list = list(range(a, b + 1))
print(x_list)

p_list = []
for x in x_list:
    prob = randint.pmf(x, low=a, high=b+1)
    p_list.append(prob)

plt.bar(x_list, p_list)
plt.show()