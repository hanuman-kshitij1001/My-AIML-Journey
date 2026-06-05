# Clip Ek Range Me Value Ko Rakhta hia 
# Matlb Jaise clip Kar dete hai na Balo me Kuch area Ko Waaise hi yaa ha bhi same kaam hota ha 
import numpy as np
m = np.array([1,2,3,4,5])
# Syntax : np.clip(array, a_min, a_max)
n = np.clip(m, a_min=2,a_max=4)
print(n)



p = np.array([5, 12, 25, 38, 45, 52, 67, 73, 88, 95])

q = np.clip(m, a_min=20, a_max=70)

print("Original Array :", p)
print("Clipped Array  :", q)