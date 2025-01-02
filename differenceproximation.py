import numpy as np
import matplotlib.pyplot as plt

dt = 0.1
t = np.arange(-2,4,0.1)

forward = (np.sin(t + dt) - np.sin(t))/dt
backward = (np.sin(t) - np.sin(t - dt))/dt
central = (np.sin(t + dt) - np.sin(t - dt))/(2*dt)


plt.plot(t,np.sin(t), label="Function sen(t)")
plt.plot(t,np.cos(t), label="Derivative cos(t)")
plt.plot(t, forward, label="Forward Difference - ERROR -> O(dt)")
plt.plot(t, backward, label="Backward Difference - ERROR -> O(dt)")
plt.plot(t, central, label="Central Difference - ERROR -> O(dt**2)")
plt.xlabel("Time")
plt.ylabel("Approximation")
plt.legend()
plt.grid()
plt.show()