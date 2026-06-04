# Numpy Kya KArta hai Put Ke # Ye Array Ke elemet Existing Element Ke jagha Kusch change karke wahi Daal Deta hai 

import numpy as np

a = np.array([11, 53, 28, 50, 38, 37, 94, 92, 5, 30, 68, 9, 78, 2, 21])
print(a)
b = np.put(a,[0,1],[110,530])
print(b)
# Note ye Mere Main Array Me CHage karta hai 

# Note kabhi kabhi kaam ata hai