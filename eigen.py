import numpy as np

A = np.array([[-0.009, 1],
              [0, -0.01]])

LI = np.array([[-0.01, 0],[0, -0.01]])

newA = A-LI

x, resids, rank, s = np.linalg.lstsq(newA, np.array([0, 0]), rcond=None)
print(x)


