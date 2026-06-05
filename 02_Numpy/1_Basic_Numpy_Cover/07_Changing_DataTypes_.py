# Dekho Hota kya hia Mai 32 Ko 64 ya fhir 64 ko 32 agera me Convert karna chahta hun to yha se change karne ka trik ye hai 
# astype  " Ye Usse Kiya jata hai Change karne ke liye "


import numpy as np

#Ex1:
a = np.array([1,2,3])
print(a.astype(np.int32))    # (3,) Out put ayagea
print(a.dtype)

#Ex2:
b = np.array([[1,2,3], [1,2,3]])
print(b.astype(np.int32))    # (2, 3) Out put ayagea
print(a.dtype)

#Ex3:
c = np.array([[[1,2,3]]])
print(c.astype(np.int32))    # (1, 1, 3) Out put ayagea
print(a.dtype)
