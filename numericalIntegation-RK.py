import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

sigma = 10
beta = 8/3
rho = 28

# Initial conditions
x0 = np.array([-8, 8, 27]) 


def rk4SingleStep(fun, dt, t0, y0):
    """fun-> Function to be evaluted"""
    f1 = fun(t0, y0)
    f2 = fun(t0 + dt/2, y0 + (dt/2)*f1)
    f3 = fun(t0 + dt/2, y0 + (dt/2)*f2)
    f4 = fun(t0 + dt, y0 + dt*f3)

    return y0 + (dt/6) * (f1 + 2*f2 + 2*f3 + f4)


def lorenz(t, y):
    dy = [sigma * (y[1] - y[0]),
          y[0] * (rho - y[2]) - y[1],
          y[0] * y[1] - beta * y[2]]
    return np.array(dy)


dt = 0.01
T = 10
timeStep = int(T/dt)
t = np.linspace(0,T,timeStep)

Y=np.zeros((3,timeStep))
Y[:,0] = x0
Yini = x0

for i in range(timeStep - 1):
    result = rk4SingleStep(lorenz, dt, t[i], Yini)
    Y[:, i + 1] = result
    Yini = result

RugeKutta = solve_ivp(lorenz, [0,T], x0, t_eval=t)

# Plot
fig = plt.figure().add_subplot(projection='3d')
plt.plot(RugeKutta.y[0, :], RugeKutta.y[1, :], RugeKutta.y[2,:], label="Ruge-Kutta", color='yellow')
plt.plot(Y[0, :], Y[1,:], Y[2,:], label="RK4", color='magenta')
plt.xlabel("Time")
plt.ylabel("X position")
plt.legend()
plt.grid(color='white', linestyle='--', linewidth=0.5)

plt.show()
