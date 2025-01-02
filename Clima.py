import numpy as np
import matplotlib.pyplot as plt


A = np.array([[0.50, 0.50, 0.25],
              [0.25, 0.00, 0.25],
              [0.25, 0.50, 0.50]])

xtoday = np.array([1.00, 0.00, 0.00])

n = int(input("Number of iterations: "))
predictions = np.zeros((n,3))
d = 2

predictions[0,:]= xtoday
for i in range(n):
    xtomorrow = A.dot(xtoday)
    predictions[i,:] = xtomorrow
    xtoday = xtomorrow
    print("Prediction N°: ",str(i+1).zfill(len(str(n))),"-->", 
          "R:",np.round(xtoday[0],d)*100,"%",
          "N:",np.round(xtoday[1],d)*100,"%",
          "C:",np.round(xtoday[2],d)*100,"%")

plt.plot(predictions)
plt.grid(True)
plt.show()

