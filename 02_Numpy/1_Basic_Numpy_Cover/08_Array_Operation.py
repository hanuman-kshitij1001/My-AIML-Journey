#  Aap Apne ArrayNumpy Me Bahut sare Mathitical Operation Kar sakte hia  Sare ke sare Aaj Nahi Sikhoge 

import numpy as np
a = np.arange(12).reshape(3,4)
b = np.arange(12, 24).reshape(3,4)
print(a)

# Yaha haam 2 Tpes Ke operation karnge 1 Scaler Operation , 2 vector Operation
# 1: Scaler matlb  : Aap Ek Single Numpy Ke Upper Ek Single Scaler number se opreate karte ho 

# Ex:1
m = a**2  # yaha Sacler 2 hai Maine a ke haar element ko 2 se multiplye kar diya 
print(m)

# Relation Opreator:
print(a>9)  # haar item se aap jake Puch rahe ho kya tum 9 se bade jaha bada honga true a jata hia 



#2: Vector Operaiton : Jab Do Numpy Array ke Uppar aap opretor Apply karte ho 
#   Do arrays (same shape wale) ke corresponding elements par operation karna.


m = np.arange(12).reshape(3,4)
n = np.arange(12, 24).reshape(3,4)
print(m+n)   # ek Element Dure Element se Solve karke ata hai 
print(m**n)
print(m/n)