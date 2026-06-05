import numpy as np
# Ye Topic Me Bahot Sare Longo Confusion Rahta hai Dhyan se padhna esse 

# Board Casting Kya hota hai : Boardcasting Ye batata Hia Ki Numpy do  diffrent Shape Wale Array Ko Kaise Treate Karta Hai While Performing Arthmati operations 
# Sabse Ye Samjh oki Boardcsating Ki Jarurat Kaha Padi
a = np.arange(6).reshape(2,3)
b = np.arange(6).reshape(2,3)
print(a)
print(b)
print()
print("Add :", a+b)

# ab Yah Dusra Code Dekhte hai Same Rakhnge bass esme k ya hia Ki Ye Alag Shape Wale Array Hia 
# Meri Marzi Hai Ki Mai inko Karma Chahta hun
a = np.arange(6).reshape(2,3)
b = np.arange(3).reshape(1,3)
print()
print(a+b)  # Add ho Raha hai Yahi Boardcasting Hai 

# Ab Mai Apko Defination Bata hun 
# haam Bordcasting tab use karte hia Jab Hamre pass 2 Diff type Ke aarays hote hai
# Eske Kuch Rules Bhi Hai Jaise 

# Rule Kewal 3 Hia Bass
#1 Make The 2 Array Have Same number of Dimension mak Size me hamesha Jayega
#Baki Rule Aur Notes me hai 
# Rule Hi Help karnge ki Andhr Kaise Adding Ho Rahi hai bhai 
# https://colab.research.google.com/drive/1RVe07-2VU4Jft8GLFyf10PrQIOVfffaR?usp=sharing#scrollTo=n2UP2iZTLPR5