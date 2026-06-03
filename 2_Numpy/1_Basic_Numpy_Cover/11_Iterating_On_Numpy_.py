#Iterating : ka Matlb hai ki Aap Simle Apne Numpy ke upper loop chala sakte ho 
import numpy as np
a1 = np.array([12,25,36])
a2 = np.array([[1,2,3], [7,8,9], [4,5,6]])
a3 = np.array([[[1,2,3], [7,8,9], [4,5,6]]])

# 1-D
for i in a1:
    print(i)

# 2-D
for i in a2:
    print(i)


# 3-D
for i in a3:
    print(i)


for i in np.nditer(a3):
    print(i)
# Ye sare Item Ko Print kar deta hai  Pahele d Ko 1-D me Lata hai aur Usse print akr deta hai sare elemnt ko 

