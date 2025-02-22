import matplotlib.pyplot as plt

a, b = 1, 5

x_list = list(range(a, b + 1))
print(x_list)

p_list = []
for x in x_list:
    prob = 1 / (b - a + 1)
    p_list.append(prob)
print(p_list)

plt.bar(x_list, p_list)
plt.show()