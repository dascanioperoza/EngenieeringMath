import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

t = np.linspace(0,1000,10000)

A = np.array([[-0.009, 1],
              [0, -0.01]])

y0 = np.array([0,1])

def funcion(t,y):
    return A@y

solution = solve_ivp(funcion,[0,1000],y0, t_eval=t)
#print(solution)

plt.plot(t, solution.y.T, label=["x", "V"])
plt.xlabel("Time")
plt.ylabel("Solution -> X & V")
plt.legend()
plt.grid()
plt.show()


