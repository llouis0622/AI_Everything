import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta, binom

a = 10
b = 10
p = 0.1

n = 38
x = 27

prior_prob = beta.pdf(p, a=a, b=b)
likelihood = binom.pmf(k=x, n=n, p=p)
post_prob = likelihood * prior_prob
print(prior_prob)
print(likelihood)
print(post_prob)

a = 10
b = 10
p_list = np.arange(0, 1, 0.01)

n = 38
x = 27
post_probs = []

for p in p_list:
    prior_prob = beta.pdf(p, a=a, b=b)
    likelihood = binom.pmf(k=x, n=n, p=p)
    post_prob = likelihood * prior_prob
    post_probs.append(post_prob)

max_prob = max(post_probs)
max_idx = post_probs.index(max_prob)
max_p = p_list[max_idx]

plt.plot(p_list, post_probs)
plt.vlines(max_p, 0, max_prob, color='red', linestyles='--')
plt.show()

print(max_prob)
print(max_idx)
post_probs[64]
p_list[64]