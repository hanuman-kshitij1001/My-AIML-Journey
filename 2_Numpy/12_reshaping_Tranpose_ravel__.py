# Reshaping Padh Liya hai Hamne Theek hai na 

# Tranpose padhte hai :
# Row Ka Col >> Col Ka ROw Kar deta hai 

import numpy as np
a = np.array([[1,2,3], [4,5,6],[7,8,9]])
print(np.transpose(a))
# eska Dusra Syntax bhi hota hai 
print(a.T)


# ravel : kitne bhi Dimension Array ko 1 -D Me Convert deta hia kitne bhi dimension ka hi array  Usse 1 D me Le ayaega 
# Ravle Kabhi Kabhar usse karenge Bhai 

b = np.array([[[1], [2], [6]]])
print(b)
c = b.ravel()
print(c)   # [1,2,3]

# Mostly tranpose Aur Reshape Use karoge jada 
# Ye New Matrix Ya Space baana ke Answer deta sam Matrix ya Arrya nahi change kartaa hai naya array bana ke return karta hai 