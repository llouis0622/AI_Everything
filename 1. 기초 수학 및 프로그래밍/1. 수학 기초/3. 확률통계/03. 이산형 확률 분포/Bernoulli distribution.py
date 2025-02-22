import matplotlib.pyplot as plt

p = 0.3

x_list = [0, 1]
p_list = []

for x in x_list:
    prob = (p ** x) * ((1 - p) ** (1 - x))
    p_list.append(prob)

plt.bar(x_list, p_list)
plt.show()