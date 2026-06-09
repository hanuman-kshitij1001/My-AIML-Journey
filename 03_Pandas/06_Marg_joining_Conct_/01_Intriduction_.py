import pandas as pd
import numpy as np

course = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/01_DataSet_courses.csv")
deliveries = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/02_Data_Set_deliveries (1).csv")
matches = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/03_Data_Set_matches.csv")
nov = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/04_Data_Set_reg-month1.csv")
dec = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/05_Data_Set_reg-month2.csv")
students = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/06_Data_Set_students.csv")

# Show ALL rows and columns
pd.set_option('display.max_rows', 0)
pd.set_option('display.max_columns', 0)
pd.set_option('display.width', 0)
pd.set_option('display.max_colwidth', 0)

print(matches)

