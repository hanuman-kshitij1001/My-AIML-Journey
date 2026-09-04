#Automatic Assessment : Ye Jo yaha pe fuction likh hun yahi usse karke haam chalne wale hai 
#1-  head and tail
#2-  sample
#3-  info
#4-  isnull
#5-  duplicated
#6-  describe

# Chalo Ek Ek Karke inko Chalte hai Hamre Table ke upper Lets Get Some Idias 

# Lets Start with pat wala table 
# Note : Programmatic Assessment → Pandas ka Hi use karna hai tumhe Theek 

# Data set :
import pandas as pd
import numpy as np
adverse_reactions = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/01_adverse_reactions.csv")
patients = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/02_patients.csv")
treatments = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/03_treatments.csv")
treatments_cut = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/04_treatments_cut.csv")

pt = patients.head()
print(pt)

# info use kar lete hai
info = patients.info()
print(info)

# Ab Haam Dekhne Wale hai kaha kaha Address nahi hai 
Missing_add = patients[patients['address'].isnull()]
print(Missing_add)  # ye 12 pat hai jo jinka data missinga hai 


# Now ab Haam Dekhne wale hai ki dubplicate data hai ki nahi 
duplicate = patients.duplicated().sum()
print(duplicate)

# Lets check on patients id kya kissi ka repeat hi raha hhai kya 
patients['patient_id'].duplicated().sum

# Aur haam given name uar sunrne ka combination check kar lete hia kya wo repeat ho raha hai hia 
rep = patients[patients.duplicated(subset=['given_name', 'surname'])]
print(rep)

# yE sara tum laga ke dekh lena tum 