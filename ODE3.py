import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

dt = 0.01
T = 10

time = np.arange(0,T,dt)

analitic = np.exp(-time) + np.exp(-2*time)


A = np.array([[ 0,  1],
              [-2, -3]])

print(np.linalg.eigvals(A))


x0 = np.array([2,-3])

def funcion(t,y):
    return A.dot(y)

solution = solve_ivp(funcion,[0,T],x0,t_eval= time)

plt.plot(time, analitic, label="Analitic Solution")
plt.plot(time, solution.y[0], label="Numerical Solution")
plt.xlabel("Time")
plt.ylabel("Position")
plt.legend()
plt.grid()
plt.show()
