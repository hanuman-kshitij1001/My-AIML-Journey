# Series with python Functionalites 
# let Start With Some Built in function 
import pandas as pd 

vk = pd.read_csv("03_Pandas/02_Pandas_Series/08_DataSet_kohli_ipl.csv")
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

# 1 len/type/dir/sorted/max/min
print(len(subs))
print(type(subs))
print(dir(subs))
print(sorted(subs))
print(min(subs))
print(max(subs))


# type conversion: 
a = list(marks_series) # yaha Hamne Esse list me convert kar diya hai 
b = dict(marks_series) # yaha Hamne Esse Dict me Convert kar diya hai 
print()
print(a)
print()
print(b)

# # membership operator: its Work On Index Value Not on index
a = '2 States (2014 film)' in movies
print(a)  # False
b = 'Aliya Bhatt' in movies
print(b)  # False

# Looping : Agr aap Chaho Toh loop Chala Sakte ho : 
# Yad Rakhna Loop Value Ke Uppar run karta hai 
for i in movies:
    print(movies)
# ab Ye Index Print karega 
for i in movies.index:
    print(i)


# opreatorns :
# arthmatic opreator(ye bahut accha example hai braodcasting ka )
a = 100-marks_series
print(a)
# you can use + , - , * , / sare Arthmatic opreatoor use kar sakte ho

# relational Opreators

m = vk >= 50
print(m) 
# yaha Apko Ek Boolean Series Milega Esse Kya Honga ki Jisme True hua Wo True Denga Warna false denga 
