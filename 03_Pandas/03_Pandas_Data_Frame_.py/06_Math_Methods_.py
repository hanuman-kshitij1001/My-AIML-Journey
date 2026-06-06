# Math Methods
# Jaise Series Me THe Waise yaha Bhi hai 


import pandas as pd
movies = pd.read_csv("03_Pandas/03_Pandas_Data_Frame_.py/02_Data_set_IPL_.csv")
ipl = pd.read_csv("03_Pandas/03_Pandas_Data_Frame_.py/03_Data_Set_movies_.csv")
student_data = [  # Esme 
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
students  = pd.DataFrame(student_data, columns=['iq','marks', 'package'])

#1: sum -> axis Argument  
# Ye Haar col ke Uppar sum apply kar detahai sari moves ko col waise
a = students.sum()
print(a)
# aap Essa Kabhi nahi Karoge Ap Genrally ek -2-3-4 col pe sum lagao ge  

b = students.sum(axis =0)
print(b)

c = students.mean(axis=1)
print(c)

d = students.var()
print(d
      
      )