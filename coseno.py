import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
import math

x = np.linspace(-10,10,2000)

#Primer Order
p1 = Polynomial([1,0])
order1 = p1(x)

#Tercer Order
p3= Polynomial([1,0,-1/math.factorial(2)])
order3 = p3(x)

#Fith Order
p5= Polynomial([1,0,-1/math.factorial(2),0,1/math.factorial(4)])
order5 = p5(x)

#Seventh Order
p7= Polynomial([1,0,-1/math.factorial(2),0,1/math.factorial(4),0, -1/math.factorial(6)])
order7 = p7(x)

#Ninthe Order
p9= Polynomial([1,0,-1/math.factorial(2),0,1/math.factorial(4),0, -1/math.factorial(6),0,1/math.factorial(8)])
order9 = p9(x)

plt.plot(x,np.cos(x),label="cos(x)")
plt.plot(x, order1,label="1er Order", linestyle='dotted')
plt.plot(x, order3,label="3er Order", linestyle='dotted')
plt.plot(x, order5,label="5th Order", linestyle='dotted')
plt.plot(x, order7,label="7th Order", linestyle='dotted')
plt.plot(x, order9,label="9th Order", linestyle='dotted')
plt.legend()
plt.axis([-10,10,-10,10])
plt.title("Taylor Series | cos(x)")
plt.grid(True)
plt.show()






