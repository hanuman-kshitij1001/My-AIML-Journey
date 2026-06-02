# Stacking  : Stacking me Kya Hota hai Ki Haam Do Se jada numoy array ko Jo sakte hai THeek hai 
# Horizontialy zodo ya vertically zodo Ye do Traika hota hai 

import numpy as np

a = np.arange(12).reshape(3,4)
b = np.arange(12, 24).reshape(3,4)

np.hstack((a,b))
np.hstack((a,b,a,b)) # h Stands For horzontal 

np.vstack((a,b,a,b)) # v Stands For horzontal 
np.vstack((a,b)) 


# jab Kai Sara Data ek Sath anlsis Karna hai toh haam Esse Jhod lete hai 
# Stacking Karne ke liye Shap same honha Chaiye 



