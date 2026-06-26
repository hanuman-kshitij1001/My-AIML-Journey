# Yaha ndim(Number of Dimensions- Yaani array kitni dimensions ka hai, ye batata hai.) ka matlb Number Of Dimension
# matlb Ap ndim ka usse karke Kiisi array ka Dimenstion pata kar sakte ho 
import numpy as np

#Ex1:
a = np.array([1,2,3])
print(a.ndim)    # 1 Out put ayagea

#Ex2:
b = np.array([[1,2,3], [1,2,3]])
print(b.ndim)    # 2 Out put ayagea

#Ex3:
c = np.array([[[1,2,3]]])
print(c.ndim)    # 3 Out put ayagea
