# Agr apke pass manlo  1 D array Hai Use 2 D me Convert kar 2 D hai Usse 3 D me 
# # Yahi kaam Hia expan_dimension Ka 

import numpy as np
a = np.random.randint(1,100,15)
print(a)
print()
b = np.expand_dims(a, axis=0)
print(b)  # Abhi Ye  1D - 2D Ho Chuka Hai 
print()


m = np.random.randint(1,100,25).reshape(5,5)
print(m)
print()
n = np.expand_dims(m, axis=1)
print(n)  # Ye Mera 3-D me Convert Ho Gaya Bro 

# Waise Ye Tarika Hia Row Vector Aur Col Vec Bannane Ka 
# Jitne Bhi ML Algo Hote hia unka kaam hota hai Prediction karne ka 


