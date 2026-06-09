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


df = students.merge(nov, how="outer", on="outer")

# esme common aur apna apna har ek cheeze dikhai deti hia 
# sab kuch a jate hai Esme Theek 
