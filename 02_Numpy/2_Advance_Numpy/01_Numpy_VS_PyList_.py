#Numpy vs list
# yaha Haam Comapre krne ke liye 3 Cheeze Choose kar rahe hai 
#1- Speed
#2- memory
#3- convenice

#1: Speed

a = [i for i in range(10000000)]
b = [i for i in range(10000000, 20000000)]

c = []
import time
start = time.time()   # time.time > hamko Current time bata deta hai 
for i in range(len(a)):
    c.append(a[i]+b[i])
print(time.time()-start)   # 1.5558502674102783  etna time mujhe Ess Pure program ko Excute karn eme laga List se 

# Ab Yahi Same kaam mai Apko Numpy Se kar ke Dikhta hun 
#numpay

import numpy as np 
m = np.arange(10000000)
n = np.arange(10000000, 20000000)
start = time.time()
c = a+b
print(time.time()-start)    # 0.16728687286376953

# Note compare ka lo ab Kitna Time Faster hai numpay Fsater hai 
# 1.5558502674102783/0.16728687286376953  = 9.30049226682  Matlb 9 hourse faster hai





#2 Ab Haam Mermory Se kasie Fayada Lete hai 
#2 Memeory 

# Yaha List se kiya 
a = [i for i in  range(10000000)]
import sys  # sys = system esme  Ek Function hOta hia ye apko Kissi Bhi variable ka kitna memeory Occupy kar raha hai Ye nikal Kar bata deta hai
m = sys.getsizeof(a)
print(m)         # 89095160-bytes Etna Memeory Occupy Kar rhaa hai 

# Yah Numpy Se kiya 
a = np.arange(10000000)
n = sys.getsizeof(a)
print(n)        #80000112

#Note Obervation :89095160 - 80000112 = 9,095,048  accha depaned bhi karta hai ki aap 64 bit usse kar rahe hi Esliye yaha Diffrent bahut kaam hai 


# Covenence Ka Matlb hia kaam Karne me Kitna Asan hai 
# Ya Apne Dekh Hi liya Kaise kaise Code Simple Hua Numpy Me as Compare to list writen in Python 
# Agr Aap Se Koi Puch le Toh Aap Ye 3 Point Bata Ke Diret bol sakte ho Hi ki Numpy Kyu Kyu Choose kiya gaya as Compare to list