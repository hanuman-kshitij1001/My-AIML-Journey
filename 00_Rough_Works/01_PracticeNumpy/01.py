import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
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

# ran = np.random.randint(1,10,(3,3))
# print(ran)


# var = np.linspace(1,10,20)
# print(var)


# a = np.identity(5, dtype=int)
# print(a)               

# a = np.arange(12).reshape(3,4)
# print("Matrix=1: " ,a)
# print()

# b = np.arange(12, 24).reshape(3,4)
# print("Matrix=1: " ,b)
# print()

# add = a+b
# print("Add: ")
# print(add)
# print()

# multiply = a*b;
# print("Multiply: ",multiply)
# print()

# print((a/b))
# print(a%b)

# a = np.random.random((3,3))
# b = np.round(a*10)
# print(b)

# # print(np.max(b))
# # print(np.sum(b))
# # print(np.prod(b))
# print(np.max(b, axis=0))


# a = np.random.random((3,4))
# b = np.round(a*10)
# print(b)
# print(np.mean(b, axis=0, dtype='int'))

# print("Varience :",np.var(b, dtype='int'))
# print("Std: ",np.std(b, dtype='int'))


# a = np.random.random((5,5))
# b = np.round(a*10)

# # print(np.ptp(b))
# arr = [1,2,3,4,5,6]
# df = pd.DataFrame(arr)
# # print(df.describe(include='all'))
# # print(df.info())
# print(df.shape)
# print(df.isnull().sum())


# c = np.arange(12).reshape(3,4)
# d = np.arange(12,24).reshape(4,3)
# print(np.dot(c,d))
# print(np.log(d))
# print(np.exp(d))

# a = np.arange(12);
# print(a.ndim)

# Slicing 

a = np.array([1,2,3,6,4,8,5])  # array[start:stop:step]
slic = a[3:5]
print(slic)