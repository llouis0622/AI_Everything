import matplotlib.pyplot as plt

p = 0.7

x_list = list(range(1, 10))
p_list = []

for x in x_list:
    prob = p * ((1 - p) ** (x - 1))
    p_list.append(prob)
print(p_list)

plt.bar(x_list, p_list)
plt.show()