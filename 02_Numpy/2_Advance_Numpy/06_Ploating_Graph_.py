import numpy as np
# Maja Ayega Bhai Ye Padhne Me 
# Numpy Ka Usse karke aap duniya Koi Bhi Graph  Bahut Jaldi Ploat kar donge Koi Graph 

#Ex1  :   x = y   >> line ka 
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y = x
plt.plot(x,y)
plt.show()

#Ex2 : y = x^2  >> Parabola
x = np.linspace(-10, 10, 100)
y = x**2
plt.plot(x,y)
plt.show()

#Ex 3: Sin X 
x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()

#Ex4 (x)log(x)
x = np.linspace(-10, 10, 100)
y = x * np.log(x)
plt.plot(x,y)
plt.show()

#Ex 5: sigmoid Graph
x = np.linspace(-10, 10, 100)
y = 1/(1+np.exp(-x))
plt.plot(x,y)
plt.show()


# Ye Sir Ne Nahi Karaya hai Ye Meri Chul Thi Maine Chat Gpt Se kara hai 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
z = [100, 200, 300, 400, 500]
ax.scatter(x, y, z)
plt.show()



