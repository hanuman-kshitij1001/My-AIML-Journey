import pandas as pd
import numpy as np

# Ess Data set pee Haam Karne wale hai Theek 
# 1st Data Frame 
patients = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/02_patients.csv")
pt = patients.head()
print(pt)

# 2nd Data Frame 
treatments = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/03_treatments.csv")
tr = treatments.head()
print(tr)

# Shap of 2nd Data Set 
shape = treatments.shape
print(shape)  # (280, 7)

# 3rd Data Frame 
adverse_reactions = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/01_adverse_reactions.csv")
ad = adverse_reactions.head()
print(ad)

# 4th Data Set 
treatments_cut = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/04_treatments_cut.csv")
tc = treatments_cut.head()
print(tc)
