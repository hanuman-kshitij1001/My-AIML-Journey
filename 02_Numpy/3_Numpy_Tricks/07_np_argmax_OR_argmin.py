# Agr matlb Agrgument max Hota hai 
# Kissi Bhi Given Axis Me uska Jo Sabse bada Element hai Uska Index Postion Nikalne ka Tarika hai 

import numpy as np
a = np.array([1,4,5,8])
b = np.argmax(a)
print(b)

# 2D me Row Wise Aur Col same kaam Karega 

c = np.random.randint(1,100,24).reshape(6,4)
print(c)
m = np.argmax(c,axis = 1) # axis = 1 Matlb row Hota hai 0 col vise
print(m)


# Note : 1-DMe esse Jada Use karte Hai 2-D me Bahut rear Use hota Hai 

# Eska Ek Bhai Hai min 
b = np.argmin(a)
print(b)