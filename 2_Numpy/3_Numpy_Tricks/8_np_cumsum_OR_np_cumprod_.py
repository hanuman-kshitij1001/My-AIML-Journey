# Jab Hame Cumulative sum Nikalna hia Ho Arrya Ka Given A axis Yahi Cumulative hia 
# ex jaise tumne 1 to 12 tak math me Obtained Marks 
# 50 60 88 90 74 68 85 97 83 90 73 69
# eska Cumulative sum Honga sum = 50 + (Sum+60) + (sum +88) + ............ = (Sum + 69)
# Har sum Ke Baad Piche Wala Sum Jode ja Rahe ho That is Cumulative sum 
# Ex Subsciber jaise Yt pe add ho rahe hai Daily 
# Gernaly Ese Sum Karne Ke Liye Haame Loop Chala Padta hai But numpy Hame Ye Function Deta hai 

import numpy as np 
a = np.array([20,85,25,3,6,])
b = np.cumsum(a)
print(b)         # [ 20 105 130 133 139]

# Ye Same Cheez Ko Aap 2-D Array pe Bhi Appy Kar sakte ho 
# Agr Aap yaha pe Axis Provide nahi akro Ge Toh Ye Usse 1-D me Convert kar denga fhir Cumsum lagayega 
c = np.random.randint(1,100,24).reshape(6,4)
print(c)
d = np.cumsum(c,axis=1)
print(d)




# Cumulative Product 
# ye Multiply kar deta hai Add nahi karta hai 
m = np.array([20,85,25,3,6,])
n = np.cumprod(a)
print(n)

# 2-D
p = np.random.randint(1,100,24).reshape(6,4)
print(p)
q = np.cumprod(c,axis=1)
print(q)