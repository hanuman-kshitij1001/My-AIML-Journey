# right Join 


import pandas as pd
import numpy as np
course = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/01_DataSet_courses.csv")
nov = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/04_Data_Set_reg-month1.csv")
dec = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/05_Data_Set_reg-month2.csv")
students = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/06_Data_Set_students.csv")

temp_df = pd.DataFrame({
    'student_id':[26,27,28],
    'name':['Nitish','Ankit','Rahul'],
    'partner':[28,26,17]
})

students = pd.concat([students,temp_df],ignore_index=True)

df = students.merge(nov,how='right',on='student_id')
# apko Yaha Ess Dikhya ga jo students me nahi hai but temp me ha itoh wo bhi data ans me dikhai denga kyu ki maine right join kiya hia 
print(df)