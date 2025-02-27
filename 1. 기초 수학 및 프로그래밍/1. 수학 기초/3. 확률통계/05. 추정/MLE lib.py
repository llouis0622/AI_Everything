import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 38
x = 27
p = 0.1

prob = binom.pmf(k=x, n=n, p=p)
print(prob)

n = 38
x = 27
p = 0.7

prob = binom.pmf(k=x, n=n, p=p)
print(prob)

n = 38
x = 27
p_list = np.arange(0, 1, 0.01)
probs = []

for p in p_list:
    prob = binom.pmf(k=x, n=n, p=p)
    probs.append(prob)

plt.plot(p_list, probs)
plt.show()

max(probs)
np.argmax(probs)
probs[71]
p_list[71]