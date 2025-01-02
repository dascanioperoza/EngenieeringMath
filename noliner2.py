import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from numpy.polynomial import Polynomial

n = 20000
T = 1000

x = np.linspace(-T,T,n)

P =(-1/3)*x**3+(1/2)*x**2


def funcion(t,y):
    A = np.array([[ np.cos(t), np.sin(t)],
                             [-np.sin(t), np.cos(t)]])
    
    return A.dot(y)


Xo = np.array([1, 0])
sol= solve_ivp(funcion,[-T,T],Xo,t_eval=x)


fig, graficos = plt.subplots(2,1)

graficos[0].plot(x, P)
graficos[0].grid(True)
graficos[0].set_xlabel('Position')
graficos[0].set_ylabel('Potential')


graficos[1].plot(sol.y[0], sol.y[1])
graficos[1].grid(True)
graficos[1].set_xlabel('Position')
graficos[1].set_ylabel('Velocity')



plt.tight_layout()
plt.show()


