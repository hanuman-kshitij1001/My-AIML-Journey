# Revsion : #Normal Indexing and Slicing
import numpy as np
a = np.arange(12).reshape(4,3)
print(a)
print(a[1,2])
print(a[1:3,1:3])

# Ab Haam Yaha Dursa Tarika Advance Tarika 
#1- Fancy Indexing
#2- Boolean Indexing


# 1: Fancy Indexing:
# agr mai Bolu 1 row, 3rd row, 4th row Nikal ke dikhao Toh Ye aap Normal Indeing se nahi nikal Paoge 
# Matlb Yaha Pe koi Patern Baan Hi Nahi Pata hai Jisse aap Indexing karo 
# Esliye En Sab ko Handle Karne ke Liye Haam Use karte hai Fancy Indexing 
# Fancy-Indexing Kya Hoti hai ki :
# Aap Same Square Braket ke Adhr Ek List pass Kar dete ho aur list me apko Jo Bhi Chahiye Hota hai Uske Index Postion De dete ho
# Ex a[[0,2,3]] ye apko 0th , 2nth , 3rd Row Ke Sare Ellement De denga Done 


#1. 1D Array me Fancy Indexing
a = np.array([10, 20, 30, 40, 50])
print(a[[0, 2, 4]])  # Syntax array[[index1, index2, index3]]
# Yahan:
# Index 0 → 10
# Index 2 → 30
# Index 4 → 50
#Ex2:
a = np.arange(12).reshape(4,3)
# print(a[[0,2,3,4]])

#2. 2D Array me Row Select Karna@  array[row_index][column_index]#
# array[row_index, column_index]
# Specific Elements Select
# Syntax: array[[row_indices],[column_indices]]


a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(a[[0,2]])  
# Output:  Yahan row 0 aur row 2 select hui.
# [[1 2 3]
#  [7 8 9]]


#3. Specific Elements Nikalna

a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(a[[0,1,2],[2,1,0]])




# arr[[row1,row2,row3], [col1,col2,col3]]  .. > Ye wala syntax Fancy Indexing me sabse important hai:








#2 Boolean Indexing : esme kya hota hai ki Jahan condition True hogi, wahi element select hoga.
# Abhi Tak Haam Index Ke Basis Kar item Nikal Rahe The Yaha Haam Condition ke basis Par Item Ko Nikalne wale Hai 
# jaise mai Bolu Mujhe Array Me Se Esse Element nikal Ke Do Jo Even Hia Yah Eska matlb Indexing Ka Kaam Nahi Hai Logic ka Kaam hai 
# Ya Mujhe Bass Wo Number jo 5 se Divisible Ho Esse Es Taraha Ke 
# Ye Bahot Usse Ful Hai BHai 

# Trick Kyahia Eski Question Se Samjha me A jati hia 

p = np.random.randint(1,100,24).reshape(6,4)
print(p)
# mai Yaha 6 row aur 4 col ki Random Genratated Array Bana raha hun Jo Ki 1 to 100 Ke Becch Ka Koi Bhi Number Pint karegi 

# chalo Espe kaam Karte hia 


#Q1 Ess array Me Mujeh Wo Numer Nikali matlb 
# Find all Number greater than 10

print(p>99)
print(p[p>10])   # [17 74 78 43 39 73 19 30 30 61 32 19 99 99 13 18 71 11 18 99 21] Ye mera Result hai yo Geting Only Those number which is Greate Than 10 
# matlb Hua Kya Ki Jaha Jaha Result Array Me True Aya Wo sari value Print kar di gai 


#Q2 Let Find Out Even Number
print(a%2==0) 
print(p[p%2 == 0])   # [90 28 62 30 68 32 78 14]


# Q3 Dono Ko Ek sath karte hia 
# print((p%2 ==0 ) & (p>10))  #  Maine Bass Try Kiya Esse hata Ke Chalane ka Toh Chal Raha hai 
print(p[(p%2 ==0 ) & (p>10)]) #  [64 70 78 74 38 34 98 88]

#Q4 Find Numner Which is not Divisible By 7
#   m = p[~(p%7 == 0)]   # ye tarika hai Dikhne ya Likhne ka
print(p[~(p%7 == 0)])  # [56]


# ye Sare Naye Array Me answer dete hia Mere Main Array Me Koi Changes Nahi akrte hai ye 

