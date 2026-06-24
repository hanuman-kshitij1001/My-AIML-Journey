import numpy as np
import matplotlib.pyplot as plt

# Array Creation 
# Sabse pahela step 
# Apko numpy import kana honga kaise 
import numpy as np
# array = [1,2,3,5]
# val = np.array(array)
# array = [1,2,3,5]
# print(val)
# print(type(val))
# print(val.shape)

# TDArray = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])
# print(TDArray)
# print(type(TDArray))
# print(TDArray.shape)


# ThrDarray = np.array([[
#     [1,2,3],
# ]])
# print(ThrDarray)
# print(ThrDarray.shape)

# newArray = np.array([
#     [
#         [1,2,3],
#         [4,5,6]
#     ],
#     [
#         [1,2,3],
#         [4,5,6]
#     ]
# ] , dtype=dict)

# print(type(newArray))
# print(newArray.shape)

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([1,2,3,4,5,6])
# y = np.array([7,8,2,4,6,9])
# plt.hist(x,y)
# plt.show()


# arrange Function in numpy 

# val = np.arange(10,1000)
# print(val)

# val = np.arange(1,50,5)
# print(val)


# Negative Step
# arr = np.arange(10, 0, -2)
# print(arr)

# arr = np.arange(0, 5, 0.2)
# print(arr)
# arr = np.arange(10, 100).reshape(3, 3, 10)
# print(arr)

ran = np.random.randint(1,10,(3,3))
print(ran)