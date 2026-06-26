import numpy as np

# linspcace kya karta hai ki ek linear range me equal points me number genrate karta hai 
# Syntax: np.linspace(start, stop, num)  or (lower_Range , Upper_Range, Number_Of_Items)
# start = kahan se shuru karna hai,  stop = kahan tak jana hai, num = kitne equally spaced numbers chahiye

a = np.linspace(-10, 10, 10)
print(a)

b = np.identity(3)  # matlb Ye 3X3 ki Natriix bana deta hai aur uske dig ko 1 aur baki sab ki 0 ana deta hai 
print(b) 
# Note Tumne Notice Kiya Honga Ki answer me " . " dot a raha ha Eska Matlb Kuch nahi by defaut float chalta hai yaha pe Bhai Esliye Agr Tum dtype = int lokh do Sab  dot haat jayega bhai 