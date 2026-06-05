# The numpy.where() function returns the indices of elements in an input array where the given condition is satisfied.
# Matlb : Mujhe yaha Conditon Ke Hisab Se Unka Imdex Mill Jata hai 

import numpy as np
a = np.random.randint(5,100, 10)
b = np.where(a>50)
print(b)

# np.where(condition, True, False)

d = np.where(a>10, 0, a)
print(d)
# Matlb Hua Kya Ki Mera Numner Agr  5 se bada hua toh 0 Kar dena Warna a Ke Element hi Rahendena hai 