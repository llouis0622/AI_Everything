import numpy as np

P = np.array([[0.1, 0.3, 0.6],
              [0.4, 0.2, 0.4],
              [0.2, 0.5, 0.3]])

P2 = np.matmul(P, P)
print(P2)

P2 = P@P
print(P2)

print(P2[0][1])

P3 = np.matmul(P2, P)
print(P3)

P3 = P@P@P
print(P3)