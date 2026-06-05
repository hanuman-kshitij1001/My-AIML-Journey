# Ek Given Array Me Multiple Items Ko Search karke Batata hai Ki wo Nultiple item Given array me hai ki nahi hai 
# Junks Of Items Search kar ne me kaam ata hai 
#  

import numpy as np
a = np.array([11, 53, 28, 50, 38, 37, 94, 92, 70, 30, 68, 9, 78, 20, 21])
item = [10,20,30,40,50,60,70]
b = np.isin(a,item)
print(b)