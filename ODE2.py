import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

time = np.arange(0,10,0.02)

x = np.exp(-time)+np.exp(-2*time)

A = np.array([[0, 1],
              [-2, -3]])

y0 = np.array([2,-3])

def funcion(t,y):
    return A.dot(y)

solution = solve_ivp(funcion,[0,10],y0, t_eval=np.arange(0,10,0.02))
print(solution)

plt.plot(time,x, label="K")
plt.plot(time, solution.y[0], label="Numeric Solution")
plt.xlabel("Time")
plt.ylabel("Position")
plt.legend()
plt.grid()
plt.show()


