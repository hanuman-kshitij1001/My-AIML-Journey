# Series Indeing Is Noting you find the number by the help of index
import pandas as pd 

vk = pd.read_csv("03_Pandas/02_Pandas_Series/08_DataSet_kohli_ipl.csv")
movies = pd.read_csv("03_Pandas/02_Pandas_Series/07_DataSet_bollywood.csv")
sub = pd.read_csv("03_Pandas/02_Pandas_Series/09_DataSet_subs.csv")
x = pd.Series([12,13,14,35,46,57,58,79,9])

#1: integer indexing
print(x)
print(x[1])
print(x[0])

#2: Negative Indexing 
# Series Negative indexing Pe kaam nahi karta hai 
# error dega 
# print(x[-1])
# Baki Sab Kaam Karega 



#2:  slicing
a = vk[5:16]
print()
print(a)  # Kuch Nahi Bass Ye 5 to 15 tak data print kar denga 

#3:  negative slicing
b = vk[-5:]
print()
print(b)  
# yaha Pe Negative Slicing Kaam Karti hia 
print()
c = movies[::2]
print(b)


#4: fancy indexing  
# Mujhe ye Pata karna hia ki [1, 3, 4, 5] match me kitne runs banaye 
d = vk[[1,3,4,5]]
print(type(vk))
print()
print(d)

# indexing with labels -> fancy indexing
d =  movies['2 States (2014 film)']