import numpy as np

A = np.array([
    [0,-2,2],
    [5,1,5],
    [1,4,-1]
])

B = np.array([
    [0,1,2],
    [3,4,5],
    [6,7,8]
])

result = A@B

print(result)