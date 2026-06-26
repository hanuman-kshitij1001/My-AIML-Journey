
import  numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)


#@ Indexing : Ek Baar me Ek Element hi nikal Paoge Ge Indexing se 
#@ Man Lo Koi Bola LAst Element batao 
print(a1[0])

#@ Chalo 2 D pe kaam karte hai 
#@ Yha Mujhe batana Padhta hia Ki Kon se ROw aur col Me Exist karta hai 
print(a2[2,3])
print(a2[1,3])
print(a2[2,2])
print(a2[0,0])


#@ Chalo Ab 3-D matrix Me Print karte hai 
#@ Sabse Pahele Hamsa Strcute ko Samjhne ki Kossis karna hai bhai 
#@ 3-D Banta hia 2 D se 

print(a3[1,0, 1])  # (kon se array me hai , row kon sa hai , col kon sa hai)





#@ Slicing : Slicing Me Ek Sath Haam Multiple Items Ko Haan Nikal sakte hai Aram se 
print(a1[2:5])  # (2 se start krunga : 5 ko nahi rakhna hai)
# Sare Concept wahi hai Jo python me padha hai 1 _ D array me 

# Chalo ab 2-D me Karte hia Slicing ko 
print(a2[0,:1])   # (kon sa Colom chahiye : kon Sa Row Chahiye)

print(a2[1,:3])

print(a2[::2,::3])



#@ 3-D me Karte hai 

a4 = np.arange(27).reshape(3,3,3)
a4[1]  # ye Bich Wala Array Hame De denga bhai Theek hai 

a4[0,1:1]   # first wala 2 d array ka 2nd row print karana hai 

a4[1,:,1]   # Second Wale numpy array Ka Bich Wala Array Chauiye 