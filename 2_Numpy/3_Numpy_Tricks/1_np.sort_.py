import numpy as np

# np.sort Apko Apke Array ko Sort Karne me Help karta hai 
# Python wala Kyu Nahi Usse kar rahe hi aWO hame List deta hai ye Numpy array return karega 
a = np.random.randint(1,100,15)
b = np.random.randint(1,100,24).reshape(6,4)
print(np.sort(a))
print()
print(np.sort(b))
# By Default Row Wiase Sort hua hia 

# Agr Apko Coloumn Waise Sort karn hai toh apko likhna hota hai axis Ka Value = 1;
print(np.sort(b,axis=0))  # ye Jo Sorting Hua HAI Col Waise Sort hua hai 

# Arg Decending Order me Sort karna hai toh Usse karna honga 
print(np.sort(a)[::-1])