import numpy as np
a = np.arange(10)  # man Lo Mujhe Eska Submation Karn hai 
print(np.sum(a))
print(np.sin(a))
print("Basi Khatam")
print()

# yaha hum Wo Sikhnge Ki Jo Built in nahi hai Unko Kaise Calculate karn ahai 

#Ex 1 Ye Bahut Famous Functuo Ml me Ya Deep Learn Me That is sigmoid functuon 
#   Eska Formula Google kar lena bhai 
def sigmoid(array):
    return 1/(1+ np.exp(-(array)))
m = np.arange(100)
print(sigmoid(m))

# 2 Loss Function 
# 1 Leanear Regration Esme Hama Mean Square Error Ka Use Karte hai 
# Jaise aap Student ke IQ ke Basic pe Uake Marsk Kitne ayega Kuch data bhi hai uska Previous ka 

actual = np.random.randint(1,50, 25)
predicated = np.random.randint(1,50, 25)
def mse(actual, predicated):
    return np.mean((actual - predicated)**2)
print(mse(actual, predicated))