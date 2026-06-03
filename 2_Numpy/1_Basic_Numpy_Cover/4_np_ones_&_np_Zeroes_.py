# Bahut Hi Jada Kaam KE hai BAhut jada use full hai 
# np.ones  kya hota hia Ki aap Esko Use karke Onthe Go numpy array bana Sakte ho jiske Sare ke sare items 1 Hote hai 
# np.Zero  kya hota hia Ki aap Esko Use karke On the Go numpy array bana Sakte ho jiske Sare ke sare items 0 Hote hai 
# Note : WHere Can You Use Its : nural Networks 
import numpy as np
a = np.ones((3, 4))
b = np.zeros((3,4), dtype=bool)
print(a)
print(b)

# agr mujeh random Number se Intilize karna hia toh Aap Likh Sakte ho 
c = np.random.random((3,4))
print(c)  # 0 Seleke 1 Tak Sare Random De Denga 