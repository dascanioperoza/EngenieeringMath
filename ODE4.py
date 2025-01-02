import numpy as np
from scipy.integrate import solve_ivp
import math
import matplotlib.pyplot as plt

A = np.array([[0, 1],
              [-2, -3]])

dt = 0.01
T = 10

x0 = np.array([2,-3])
t = np.arange(0,T,dt)

def funcion(t,y):
    return A.dot(y)

solution = solve_ivp(funcion,[0,T],x0,t_eval=np.arange(0,T,dt))

fig, graficos = plt.subplots(2,1)

graficos[0].plot(solution.t, solution.y[0], label="Numerical Solution")
graficos[0].plot(t, np.exp(-t)+np.exp(-2*t),  label="Analitical Solution")
graficos[0].grid(True)
graficos[0].set_xlabel('Time')
graficos[0].set_ylabel('Position')
graficos[0].legend()

graficos[1].plot(solution.y[0], solution.y[1])
graficos[1].grid(True)
graficos[1].set_xlabel('Position')
graficos[1].set_ylabel('Velocity')

plt.tight_layout()
plt.show()

