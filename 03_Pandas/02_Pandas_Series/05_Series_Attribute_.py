# Haam Kay KAr rahe hi aki series class ke Object bana rahe hi a
# Yaha Haam Series Ke Kuch bahut jada import attribute batane wale hia bahut imp 

#1: size
import pandas as pd
marks = pd.Series([82,96,85,45,65,87,100])
print(marks.size)


marks2 = {
    'maths' : 67,
    'English':85,
    'Hindi':89,
    'Physics':100,
    "Advance Backchodi":1000
}

print(marks.size)


#2: dtype 
# ye bata Deta hai Apke series Ke ander data types kya hai 
data_type = pd.Series(marks)
print(data_type.dtype)  # int64

#:3 name: 
#names = pd.series(marks)
print(marks.name)

#4: is_unique: Ye ye Batata Hia Ki Apke Series Ke Sare Item Unique hai ya Nahi 
print(marks.is_unique) # True

#5: index : Esko Call Karne Se series me Jitne bhi Index wo Mill Jate hai 
print(marks.index)  
# RangeIndex(start=0, stop=7, step=1)

#6: Values : Ye hame 
print(marks.values)
# Ye apko Sare ke sare marks Nikal Kar de deta hai Ye hamne Numoy Array Deta hai 
#  [82  96  85  45  65  87 100]