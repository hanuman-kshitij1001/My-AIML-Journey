# Missing Values Kya Hoti hai :
# | Name  | Age   | Salary |
# | ----- | ----- | ------ |
# | Ram   | 22    | 30000  |
# | Shyam | **?** | 40000  |
# | Mohan | 25    |   ?    |
# Yahan Age aur Salary ki kuch values missing hain
# NumPy me Missing Values
# Usually missing values ko np.nan (Not a Number) se represent karte hain.
# nan or none dono same nahi hai Hamesaha nan hi use kiya jata hau nan
# kya Logic hai Esse Solve karne Wo Karte hai sare missing Values Ko Hata dete hai Bass
# Yaha Haam Karenge boolean Indexing

import numpy as np
a = np.array([1,2,3,4,np.nan,6])
print(a)

# "isnan" ye ek function ye har item se jake puchega ki kya tum missing value ho ?
# Esse Apko Bollean Me false mil jayega Uss Jagha pe
# Phir Wahi Convert karo Ese Apko True Banna Honga "~ " use karke 
# Ap Bass Etna Yad Rakho baas Mujhe Sari Missing Values Hata Deni hai   