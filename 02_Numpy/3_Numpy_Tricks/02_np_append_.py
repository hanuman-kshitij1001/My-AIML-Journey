# Python Ke Append Ke Jaise Hi Hai 
import numpy as np
a = np.random.randint(1,100,15) 
b = np.random.randint(1,100,24).reshape(6,4)

print(a)
# [6 64 41 74 72 30 20 18 81 45 51 85 52 35 87]

print()

c = np.append(a,200)
print(c)
# [  6  64  41  74  72  30  20  18  81  45  51  85  52  35  87 200]


# You Want to Append in 2-D array Also 

d = np.append(b,np.ones((b.shape[0],1)), axis = 1)
print(d)
# Esse Last me hamne 1,1,1, ... ka Ek Coloum Apend Kar diya hia