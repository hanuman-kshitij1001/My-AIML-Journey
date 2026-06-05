# Ye Python me Jaise Loop CHalte waqt range  padha Tha Ye Waise hi hai Bhai
# np.arange
import numpy as np

#1: Syntax: np.array(start, end)
a = np.arange(1,11)  # Ye Ek  numpyarray banata hai from 1 to 10 
print(a)             # [ 1  2  3  4  5  6  7  8  9 10] 

#2: Syntax: np.array(start, end, Yaha Jo Number Hota hia Ittration Decide karta hia )
b = np.arange(1, 50,5)
print(b)     # [ 1  6 11 16 21 26 31 36 41 46] 
             #   Matlb 1+5 = 6 continue 5  add in Your number
