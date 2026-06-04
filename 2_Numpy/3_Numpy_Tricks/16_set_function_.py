import numpy as np

m = np.array([1,2,3,4,5])
n = np.array([3,4,5,6,7])

a = np.union1d(m,n)
print(a)

b = np.intersect1d(m, n)
print(b)

c = np.setdiff1d(m, n)
print(c)

d = np.setxor1d(m,n)
print(d)

# e = np.in1d(m, n)
# print(e)
# Eske Jagha Sayad 
e = np.isin(m, n)
print(e)
# Use hota hai 