import pandas as pd

# yaha pe Sabse Pahele Haam Kya Padhnge Wo hai ki series pandas theek hai na 

# data  = [1,2,5,3,8,'kshitij',3,True,9]
# print(data)

# df = pd.Series(data)
# print(df)

# print(df.dtype)

# Now We Mobe to point Ki Data create karne ke kitne traike Hai series me pandas me 
# 2 Dict
# data  = {
#     'a' : '10',
#     'b' : '20',
#     'c' : '30',
#     'd' : '40',
#     'e' : '50'
# }

# df = pd.Series(data)
# print(df, "\n" ,df.dtype)

#3 Scaler value se 
# df = pd.Series(10, index=[1,2,3,4,5,6])
# print(df)


# # List , custome index 
# df = pd.Series([1,2,3,4,5], index=[10,20,30,40,50])
# print(df)

# You are pasing the tupple Bro here done
# df = pd.Series((1,2,3,54,8))
# print(df)


# Series Attribute 

data = [1,2,2,2,36,8,5,8,5]
df = pd.Series(data)
print(df.is_unique)
print()
data = {
    'a' : '100',
    'b' : '101',
    'c' : '102',
    'd' : '103',
    'e' : '104',
    'f' : '105',
    'f' : '105',
    'f' : '105',
    'f' : '105'
}
df = pd.Series(data)

# df = pd.Series(data)
# print("Size of the series: ",df.size)
# print(df)

# dtype
print(df.dtype)

#name
print(df.name)  

# is_unique
print(df.is_unique) # But ye dect me true kyu de raha hai pata nahi yaro 

# index 
print(df.index)

# values
print(df.values)

idx = pd.RangeIndex(start=0, stop=9, step=1)
print(idx)
df = pd.Series(data, index = idx)
print(df)


