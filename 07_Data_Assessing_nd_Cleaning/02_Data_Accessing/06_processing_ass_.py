# Sabse Pahele Haam # export data for manual assessment

import pandas as pd
import numpy as np

# Load datasets
adverse_reactions = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/01_adverse_reactions.csv")
patients = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/02_patients.csv")
treatments = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/03_treatments.csv")
treatments_cut = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/04_treatments_cut.csv")


# Bhai ye code multiple DataFrames ko ek hi Excel file ke alag-alag sheets mein save kar raha hai. ✅

# Create a single Excel workbook for manual assessment
# Each DataFrame will be stored in a separate sheet

with pd.ExcelWriter("clinical_trials.xlsx") as writer:

    # Sheet 1: Patients dataset
    patients.to_excel(writer, sheet_name="patients")

    # Sheet 2: Treatments dataset
    treatments.to_excel(writer, sheet_name="treatments")

    # Sheet 3: Treatments Cut dataset
    treatments_cut.to_excel(writer, sheet_name="treatments_cut")

    # Sheet 4: Adverse Reactions dataset
    adverse_reactions.to_excel(writer, sheet_name="adverse_reactions")


# Final Excel File
# Excel khologe to kuch aisa dikhega:
# clinical_trials.xlsx
# ├── patients
# ├── treatments
# ├── treatments_cut
# └── adverse_reactions
# Ek workbook ke andar 4 sheets.