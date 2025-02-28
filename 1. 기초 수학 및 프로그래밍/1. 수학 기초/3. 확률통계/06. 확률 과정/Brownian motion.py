import numpy as np
import matplotlib.pyplot as plt

np.random.seed(777)

n = 1000
Bt = np.random.normal(loc=0, scale=1, size=n-1)
Bt = np.insert(Bt, obj=0, values=0)
Bt_cumulative_sum = Bt.cumsum()

plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.plot(Bt)
plt.title('Brownian Motion Increments')
plt.subplot(2, 1, 2)
plt.plot(Bt_cumulative_sum)
plt.title('Brownian Motion Path')
plt.show()

mean_Bt = np.mean(Bt)
var_Bt = np.var(Bt)
print(mean_Bt)
print(var_Bt)

n = len(Bt)
t = 2
B2 = []
for i in range(t, n - 1):
    B = np.sum(Bt[i - t + 1:i + 1])
    B2.append(B)
print(np.mean(B2))
print(np.var(B2))