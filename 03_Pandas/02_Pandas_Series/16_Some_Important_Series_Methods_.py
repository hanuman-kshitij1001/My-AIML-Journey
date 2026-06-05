# astype
# between
# clip
# drop_duplicates
# isnull
# dropna
# fillna
# isin
# apply
# copy

import numpy as np
import pandas as pd
vk = pd.read_csv("03_Pandas/02_Pandas_Series/08_DataSet_kohli_ipl.csv").squeeze('columns')
movies = pd.read_csv("03_Pandas/02_Pandas_Series/07_DataSet_bollywood.csv")
subs = pd.read_csv("03_Pandas/02_Pandas_Series/09_DataSet_subs.csv")
x = pd.Series([12,13,14,35,46,57,58,79,9])
marks = [82,96,85,45,65,87,100]
subjects = ['maths', 'english', 'Hindi', 'Science', 'History', 'UPSC', 'Physics']
marks = {
    'maths' : 67,
    'English':85,
    'Hindi':89,
    'Physics':100,
    "Advance Backchodi":1000
}
marks_series = pd.Series(marks)      


# Now Start bro 

#1: astype
subs = pd.read_csv("03_Pandas/02_Pandas_Series/09_DataSet_subs.csv").squeeze('columns')
print(subs)



#between
# vk = pd.read_cvc("03_Pandas/02_Pandas_Series/08_DataSet_kohli_ipl.csv").squeeze('columns')
# print(vk)

# clip
subs = pd.read_csv(
    "03_Pandas/02_Pandas_Series/09_DataSet_subs.csv"
).squeeze('columns')
print(subs.clip(50, 200))

print(subs.clip(100,200))

# # drop_duplicates
temp = pd.Series([1,1,2,2,3,3,4,4])
print(temp)
a = temp.drop_duplicates(keep='last')
print(a)
# Output me temp change nahi hoga.
#default me nayi Series return karta hai, original ko modify nahi karta.


# isnull : Data me missing values (NaN, None) ko identify karna.
# ye batata hai:\
# Missing value hai → True
# Missing value nahi hai → False
s = pd.Series([10, 20, np.nan, 40, None])
print(s.isnull())


## dropna  .. Missing values (NaN, None) wali rows ko hata dena.
s = pd.Series([10, 20, np.nan, 40, None, 60])
print(s)
print(s.dropna())
# Output
# Dekho:
# NaN wali entries gayab ho gayi.
# Index same raha (0,1,3,5).
# Original Series change nahi hoti


# isnull()       vs             dropna()

# Method	                Kaam
# isnull()	                Missing values dhoondho
# isnull().sum()	        Missing values count karo
# dropna()	                Missing values hata do
# fillna()	                Missing values ko kisi value se bhar do


# fillna .. Missing values (NaN) ko kisi value se bhar dena.
temp = pd.Series([10, 20, np.nan, 40, np.nan, 60])
print(temp)
print(temp.fillna(0))


# isin >> "Kya ye value is list/set me maujood hai?"  Ye har element ke liye True ya False return karta hai.
s = pd.Series([10, 20, 30, 40, 50])
print(s.isin([20, 40]))

# apply() ka matlab:
# Series ke har element par ek function lagao.
s = pd.Series([1, 2, 3, 4, 5])

def square(x):
    return x * x
print(s.apply(square))

# Example 2 (Lambda)
print(s.apply(lambda x: x * 10))


# copy() ka matlab:
# Original data ki independent copy banao.
a = pd.Series([10,20,30])
b = a
b[0] = 999
print(a)
# a bhi change ho gaya.
#Kyuki:
#b = a
# copy nahi banata.
# Dono same object ko point kar rahe hote hain.

# Solution: copy()
a = pd.Series([10,20,30])
b = a.copy()
b[0] = 999
print(a)
# Original safe rahega.
# Without copy:
# a ───► [10,20,30]
#           ▲
#           │
# b ─────────

# With copy:
# a ───► [10,20,30]
# b ───► [10,20,30]
# Dono alag objects hain.