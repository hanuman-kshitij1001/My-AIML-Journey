import pandas as pd
import numpy as np
nov = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/04_Data_Set_reg-month1.csv")
dec = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/05_Data_Set_reg-month2.csv")
students = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/06_Data_Set_students.csv")

# There  are four types of join 
# 1: inner join
# 2: left join
# 3: right join
# 4: outer join




# Inner Join: 
# Apke pass do tables hai ek aap bula rahe ho left table dusre ko right table 
# Apko agr ubko inner join karna hai toh basicly ap esse items ko nikalte ho jo dono me present ho 
# matlb aap Common items Ko nikal chahte ho 

# students me there are 25 students me 
# dec me me  regs bol rahe hai esse esme 58 ke ass pass students hai 
# ab Ye socho jab inner join honga toh kon se col pe honga 
# hamesha ek Common col honga jisse ap join kar paoge 
# inner hai eska matlb common students hi dikhaa denge jo student id studetns me hai aur apke dec data set me hai 


# chalo mai Inner join likhte hai 
# jo bhi  sabse pahele ata hai wo left tabel ban jata hai jase yaha students secon table se dec jo box me likha jata hai
# # ek Aur parameter hota hai " how "ka Wo ye batata hia ki kiss traha ka join karna hai left , rigt , etc  
# Ek Aur pracmerter hai " on "  me aap batate ho ki kon se coloumn ke basis pe joing karoge 

df = students.merge(dec, how ='inner', on ='student_id')
print(df)