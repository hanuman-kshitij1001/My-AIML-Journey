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

# a = np.array([1,2,3,6,4,8,5])  # array[start:stop:step]
# slic = a[3:5]
# print(slic)


# a = np.array([1,2,3,4,5])
# b = np.array([6,7,8,9,2])
# print(a.concat(b))

# Seed function 

# np.random.seed(42)
# var = np.random.random(3).astype(int) 
# b = np.round(var*100,0).astype(int)
# print(var)
# print(b)

# pehle array bana, BAAD MEIN badlo
# var = np.array([1.5, 2.7, 3.9])   # pehle bana
# var2 = var.astype(int)             # baad mein badla
# print(var2)

# rang = np.random.default_rng(42)
# print(rang)
# val = rang.integers(low = 10, high=5852000, size=5)
# print(val)


#  Ditribution 
# rng = np.random.default_rng(42)

# val1 = rng.uniform(low=0, high=10, size=5)   # 0-10 ke beech
# val2 = rng.normal(loc=5, scale=1, size=5)    # beech mein zyada
# val3 = rng.binomial(n=10, p=0.5, size=5)     # 0-10 ke beech integers

# print(val1)
# print(val2)
# print(val3)


# student = np.arange(124,180)
# val = student.reshape(5,-1)
# print(val)
# print()
# new = val.flatten()
# print(new)
# print()
# val2 = new.resize()
# print(val2)

# a = np.arange(6)
# b = np.arange(5,11)
# result = np.vstack([a,b])
# print(result)
# print()
# c = np.arange(10,12)
# d = np.arange(9,15)
# result = np.hstack([c,d])
# print(result)

# spliting'
# arr = np.array([1,5,3,9,5,7,5,9,5])
# result = np.split(arr, 3)  # Zarori hai ki array barabar tukdon mein bate!
# print(result)

# arr = np.array([[1, 2, 3,4],
#                 [4, 5, 6,7],
#                 [7, 8, 9,3],
#                 [10,11,12,10]])

# result = np.hsplit(arr,2)
# print(result)
# print(result[0])

# Vectorization

#  Ye ha Normal Zindagi 
# marks = [10, 20, 30, 40, 50] 
# new_marks = []
# for mark in marks:
#     new_marks.append(mark+5)
# print(new_marks)

# Ab Dekho mentos jindgi 
marks = np.array([10, 20, 30, 40, 50]) 
new_marks = marks + 5
print(new_marks)


import time
data = list(range(1000000))
arr = np.array(data)

#  Oython Loop se karu toh kya Honga 

start = time.time()
result = [x * 2 for x in data]
print(f"Loop time: {time.time() - start:.4f} seconds")

# NumPy Vectorized
start = time.time()
result = arr * 2
print(f"NumPy time: {time.time() - start:.4f} seconds")