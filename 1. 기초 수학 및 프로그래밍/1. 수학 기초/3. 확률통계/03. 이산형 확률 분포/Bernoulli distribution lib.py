import matplotlib.pyplot as plt
from scipy.stats import bernoulli

p = 0.3

x_list = [0, 1]
p_list = []

for x in x_list:
    prob = bernoulli.pmf(k=x, p=p)
    p_list.append(prob)

plt.bar(x_list, p_list)
plt.show()