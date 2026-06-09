# yaha Pe Haam 
# wo table me haam na common chezo ko print karte hia balki un cheezo ko bhi print karte ho jo left wale table me hai 
# but right wale table me nahi hai 


import pandas as pd
import numpy as np
course = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/01_DataSet_courses.csv")
nov = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/04_Data_Set_reg-month1.csv")
dec = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/05_Data_Set_reg-month2.csv")

df = course.merge(dec, how="left", on="course_id")
print(df)