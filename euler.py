import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
import math

x = np.linspace(-10,10,2000)

aproximation = np.cos(x) + 1j*np.sin(x)

#Primer Order
p1= Polynomial([1, 1j])
order1 = p1(x)

#Segundo Order
p2= Polynomial([1, 1j, -1/math.factorial(2)])
order2 = p2(x)

#Tercer Order
p3= Polynomial([1, 1j, -1/math.factorial(2),-1j/math.factorial(3)])
order3 = p3(x)

#Cuarto Order
p4= Polynomial([1, 1j, -1/math.factorial(2),-1j/math.factorial(3),1/math.factorial(4)])
order4 = p4(x)

#Quinto Order
p5= Polynomial([1, 1j, -1/math.factorial(2),-1j/math.factorial(3),1/math.factorial(4),1j/math.factorial(5)])
order5 = p5(x)

#Sexto Order
p6= Polynomial([1, 1j, -1/math.factorial(2),-1j/math.factorial(3),1/math.factorial(4),1j/math.factorial(5), -1/math.factorial(6)])
order6 = p6(x)

plt.plot(x,np.exp(1j*x),label="e**(ix)")
plt.plot(x,aproximation,label="cos(x)+isen(x)")
plt.plot(x, order1,label="1er Order", linestyle='dotted')
plt.plot(x, order2,label="2nd Order", linestyle='dotted')
plt.plot(x, order3,label="3er Order", linestyle='dotted')
plt.plot(x, order4,label="4th Order", linestyle='dotted')
plt.plot(x, order5,label="5th Order", linestyle='dotted')
plt.plot(x, order6,label="6th Order", linestyle='dotted')

plt.legend()
plt.axis([-10,10,-10,10])
plt.title("Taylor Series | e**(ix)")
plt.grid(True)
plt.show()






