# 1b. Data Accessing
# In this step, the data is to be understood more deeply. Before implementing methods to clean it, you will definitely need to have a better idea about what the data is about.



# Data assessment ka matlab hota hai data ko evaluate (jaanchna) karna
# taaki pata chale ki data analysis ya machine learning ke liye suitable hai ya nahi.

# Isme hum check karte hain:
#1- Data Quality
#2- Data Completeness
#3- Data Consistency
#4- Data Accuracy
#5- Data Relevance

# Example  : Maan lo tumhare paas students ka dataset hai:
# | Name | Age  | Marks |
# | ---- | ---- | ----- |
# | A    | 20   | 85    |
# | B    | NULL | 90    |
# | C    | 150  | 78    |

# Data assessment mein hum dekhenge:
#1-  B ki age missing hai ❌
#2-  C ki age 150 hai (unrealistic) ❌
# Toh data ko clean karna padega.

# AIML Perspective
# Machine Learning project mein data assessment usually EDA (Exploratory Data Analysis) 
# aur Data Cleaning se pehle ya uske saath kiya jata hai taaki model ko high-quality data mile.
#Data Assessment = Data ki quality, accuracy, completeness aur usefulness ko check karne ki process.



# Types of Unclean Data
# There are 2 kinds of unclean data

#1- Dirty Data  : Dirty Data (Data with Quality issues): Dirty data, also known as low quality data. Low quality data has content issues.
# Yaha Pe Wo Chaaze Hoti hai Jo Nahi Honi Chaiye 
# Ex : 
# Missing values (NULL)
# Duplicated data
# Missing Data
# Corrupt Data
# Inaccurate Data

#2. Messy Data: 
# Basically Essa Data JO part hai Uss data But Wo apne Sahi Jagha pe nahi hai That Is called Messy data
# Messy Data (Data with tidiness issues):
#                                       Messy data, also known as untidy data. Untidy data has structural issues(Matlb uske Structre me Problem hai ).Tidy data has the following

# properties: Agr Ye 3 property Full Fill nahi ho rahi hia eska matlb apka data messy data hai Ya untidy data hai 
#1- Each variable forms a column
#2- Each observation forms a row
#3- Each observational unit forms a table



# Set Up 
import pandas as pd
import numpy as np
adverse_reactions = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/01_adverse_reactions.csv")
patients = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/02_patients.csv")
treatments = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/03_treatments.csv")
treatments_cut = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/04_treatments_cut.csv")

print(adverse_reactions)
print(patients)
print(treatments)
print(treatments_cut)