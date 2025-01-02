import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
import math

x = np.linspace(-10,10,2000)

#Primer Order
p1 = Polynomial([0, 1])
order1 = p1(x)

#Tercer Order
p3= Polynomial([0,1,0,-1/math.factorial(3)])
order3 = p3(x)

#Fith Order
p5= Polynomial([0,1,0,-1/math.factorial(3),0,1/math.factorial(5)])
order5 = p5(x)

#Seventh Order
p7= Polynomial([0,1,0,-1/math.factorial(3),0,1/math.factorial(5),0, -1/math.factorial(7)])
order7 = p7(x)

plt.plot(x,np.sin(x),label="sin(x)")
plt.plot(x, order1,label="1er Order", linestyle='dotted')
plt.plot(x, order3,label="3er Order", linestyle='dotted')
plt.plot(x, order5,label="5th Order", linestyle='dotted')
plt.plot(x, order7,label="7th Order", linestyle='dotted')
plt.legend()
plt.axis([-10,10,-10,10])
plt.title("Taylor Series | sin(x)")
plt.grid(True)
plt.show()






