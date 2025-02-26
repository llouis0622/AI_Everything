import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

a, b = 0.5, 0.5
xs = np.arange(0.01, 1, 0.01)
ps = []

for x in xs:
    prob = beta.pdf(x, a=a, b=b)
    ps.append(prob)

plt.plot(xs, ps)
plt.show()