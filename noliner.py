import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

n = 200
T = 10

tiempo = np.linspace(0,T,n)

def funcion(t,y):
    A = np.exp(-t)*np.array([[ np.cos(2*t), np.sin(2*t)],
                             [-np.sin(2*t), np.cos(2*t)]])
    
    return A.dot(y)


Xo = np.array([1, 0])
sol= solve_ivp(funcion,[0,T],Xo,t_eval=tiempo)


plt.plot(sol.y[0], sol.y[1],label="Solution")

plt.xlabel("Position")
plt.ylabel("Velocity")
plt.legend()
plt.grid()
plt.show()

