import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import math

n = 10000
a = 0
b = 10

dx = (b-a)/n 

integralDefinida = integrate.quad(lambda x: np.sin(x), 0, 10)

rightSolution = 0

for k in range(1,n):
    rightSolution += math.sin(a + k*dx)*dx

leftSolution = 0

for k in range(0,n-1):
    leftSolution += math.sin(a + k*dx)*dx

print("Integral Definida: ", integralDefinida[0])
print("Right Solution: ", rightSolution)
print("Left Solution: ", leftSolution)

print("Trapezoidal Integration: ", (rightSolution + leftSolution)/2 )


