import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

w = 2*np.pi #Natural frequency
d = 0.25 # Damping ratio

A = np.array([[0, 1], 
              [-w**2, -2*d*w]])

dt = 0.01 # Time step
T = 10 # Time to integrate

x0 = np.array([2, 0]) # Initial conditions

iterations = int(T/dt)
timeSteps = np.linspace(0,T, iterations)

# Forward Euler
xF = np.zeros((2, iterations))
xF[:, 0] = x0

for k in range(iterations -1):
    xF[:, k+1] = (np.eye(2) + dt*A)@xF[:, k]

# Backward Euler

xB = np.zeros((2, iterations))
xB[:, 0] = x0

for k in range(iterations -1):
    xB[:, k+1] = np.linalg.inv(np.eye(2) - dt*A)@xB[:, k]

# Ruge-Kutta
RugeKutta= solve_ivp(lambda t,y:A@y,[0,T],x0,t_eval=timeSteps)

# Plot
fig = plt.figure()
fig.patch.set_facecolor('black')

ax = plt.gca()
ax.set_facecolor('black')
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

plt.plot(timeSteps, RugeKutta.y[0, :], label="Ruge-Kutta", color='yellow')
plt.plot(timeSteps, xF[0, :], label="Forward Euler", color='cyan')
plt.plot(timeSteps, xB[0, :], label="Backward Euler", color='magenta')
plt.xlabel("Time", color="white")
plt.ylabel("X position", color="white")
plt.legend()
plt.grid(color='white', linestyle='--', linewidth=0.5)

plt.show()
