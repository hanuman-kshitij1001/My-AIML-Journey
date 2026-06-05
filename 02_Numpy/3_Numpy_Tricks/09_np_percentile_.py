# Aap compute the nth percentile of given data along the Specified Axis

import numpy as np
a = np.random.randint(1,100,15) 

# 100 Percentile Sabse Max Hot hai 
b = np.percentile(a,100)
print(b)   # 95.0 Ye Out put Bata raha hia Ki Koi Bhi Esme Se Number 95 se jada nahi  haai 

# zero Percentile sabse min Hota hai 
c = np.percentile(a,0)
print(c)  # 2.0


# Sabse 50 Bech wala Hota hai Matlb Adhe Usse Age Hai Adhe Usse piche hia 

d = np.percentile(a,50)
print(d)   # 52.0

# percentile Formula = P = (n/N)x100

