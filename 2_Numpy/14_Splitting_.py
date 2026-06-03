# Spliting : Ye Stacking ka Ulta Hota hai Haam Yah Pe Array ko Cut dete hai 
# Yaha Bhi Do Tarike se cut karte hia Horz aur Vertically 

import numpy as np

a = np.arange(12).reshape(3,4)
b = np.arange(12, 24).reshape(3,4)

np.hsplit(a,2)  # (arrya name , kitne part me katna chahate ho)
np.vsplit(a,3)  # Ye apke 3 No Rows Ko Alg Kar dega 


# Ek Data Soce Se multiple Cheeze bante hi toh waha pe Splite ka kaam ata hai 























