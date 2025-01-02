import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0,10,2000)

x =  0.5*np.exp(-t) + np.exp(-2*t) +0.5*np.exp(-3*t)

plt.plot(t,x,label="Solution")
plt.xlabel("Time")
plt.ylabel("X(t)")
plt.legend()
plt.grid()
plt.show()



