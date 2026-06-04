# Flip Ka Kaam Hota hai ki  Ki Array Ko Revse KAr deta hai Matlb Usse Mirrir Image Deta hai 
# Bass Yahi Hota hia Flip 

import numpy as np

a = np.array([11, 53, 28, 50, 38, 37, 94, 92, 70, 30, 68, 9, 78, 20, 21])
b = np.flip(a)
print(b)


# 2-D Me Bhi Kar sakte hai 
m = np.random.randint(1,100,25).reshape(5,5)
n = np.flip(b,axis=0)
print(n)

# Bhut Use full Nahi But Kaam A sakta hai 