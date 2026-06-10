#Note 99 % time aap inner join hi usse karne wale ho theek hai na 

# Chalo Data Set Add kar lete hai 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

course = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/01_DataSet_courses.csv")
deliveries = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/02_Data_Set_deliveries (1).csv")
matches = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/03_Data_Set_matches.csv")
nov = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/04_Data_Set_reg-month1.csv")
dec = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/05_Data_Set_reg-month2.csv")
students = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/06_Data_Set_students.csv")

# 1. find total revenue generated

df = nov.merge(course, how='inner', on="course_id")['price'].sum()
print(df)



# 2. find month by month revenue

temp_df = pd.concat([nov, dec], keys=['Nov', "Dc"]).reset_index()
temp_df.merge(course,on='course_id').groupby('level_0')['price'].sum()

# 3. Print the registration table 
# cols -> name -> course -> price
df = nov.merge(students,on='student_id').merge(course,on='course_id')[['name','course_name','price']]
print(df) # Yaha Pe Hamne 3 Table ko Join kiya hai Hme yaha 3 bar marge kiya 


#4. Plot bar chart for revenue/course

df = nov.merge(course,on='course_id').groupby('course_name')['price'].sum().plot(kind='bar')
# plt.show()


# 5. find students who enrolled in both the months
common_student_id = np.intersect1d(nov['student_id'],dec['student_id'])
print(common_student_id)