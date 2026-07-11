import numpy as np


# reshape : Ek given Numpy Array ko Kissi Durse Shape me Convert deta hai 

# a = np.arange(1, 11).reshape(5,2)    # syntax: array.reshape(rows, columns)
# print(a)                             
# Actually Yah Hua Kya Ki Maine mere range wale array ko Reshape kar diya 2_d Array me 
# Note : eshape se array ko 2D, 3D, 4D, 5D ... kisi bhi dimension me convert kar sakte ho, bas total elements same rehne chahiye.
# Note2; a.reshape(2, 5, 12) Yaha 3 Values Hai Eska Matlb ye Yaha 3_d array hai  (shape)  = (depth, rows, cols)
# Same For 4, 5,6 Etc D ke liye bhi 


# np ones and np zeros 
val = np.ones((3,3) )
print(val)

val = np.zeros((3,3) )
print(val)


val = np.ones((3,3), dtype='bool' )
print(val)

val = np.eye((3,3))
print(val)


