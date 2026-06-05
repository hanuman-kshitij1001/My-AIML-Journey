# Ye Kay Karta hai Ki Freq Count batata hia in a given range
# Numpy has a built-in numpy.histogram() function which represents the frequency of data distribution in the graphical form.

import numpy as np
a = np.array([11, 53, 28, 50, 38, 37, 94, 92, 5, 30, 68, 9, 78, 2, 21])

b = np.histogram(a, bins=[0,10,20,30,40,50,60,70,80,90,100])
print(b)

# It is important static Point of View 
