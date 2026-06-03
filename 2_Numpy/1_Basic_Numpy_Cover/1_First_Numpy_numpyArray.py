# How We can Create Numpy Array 
# Step 1: Sabse Pahele Hame numpy ko import karna padta hai 
import numpy as np

#Step 2: ab apa Numpy Array Create kar sakte ho Using Finction Called "np.array" se
var = np.array([1,2,3,4])  # Waise Esko Kuch nahi chahiye esse basicly Ek Liist Chahiye Andhr me 
print(var) # apka Ko Yaha Se numpy Array Mill Jayega 
print(type(var)) # ye Apko Batayega Ki ye Numpy Array hai 


# We Can Create 2-D array As Well as 
b = np.array([[1,2,3],[4,5,6]])
print(b)

# 3-D numpy 
c = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(c)


# Note :
#1: Pahla Array 1-D called As Vector
#2: Dusra Array 2-D Array Apna Usse haam matrix Bolte hai 
#3: Third Is Called tensor
# Ess Traha Se aap 4,5,6 ... Kitne bhi dimension ka Ek NumpiArray Bana Sakte ho 


# Abhi Tak Jitne Bhi Haamne Data Use kiya hai Wo sare ke sare integer the Haam Esse Kisssi Bhi Type Ka Ban sakte hai 
# Jaise :
# yaha Mai float ka Bana Raha hun 
# Apko Kuch nahi karn hai 
# Bass Likhna hai np.array([1,2,3], dtype=float)  
# bass etna List banne ke baad bass apko "dtype = data_type" Ye Likhna Maat bhulna 
#Ex:1
d = np.array([1,2,3], dtype=float) 
print(d)
#Ex:2 
e = np.array([1,2,3], dtype=bool) 
print(e)
#Ex:3
f = np.array([1,2,3], dtype = complex)
print(f)

# Note : Float jada use karte hai haam bhai 