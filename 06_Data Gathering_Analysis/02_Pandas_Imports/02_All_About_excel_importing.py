# Step 1 Sabse Pahle Wahi 
# import karo pandas ko 
import pandas as pd 

# step 2 Actual Syntax 
pd.read_excel("Yhaa par baas Apko apni file ka Name bata dena hai")
# aur Ye Excel ki files hamesha  (.xlsx, .xls) form me hi hoti hai theek hai na 

# Agar Error Aaye
# pip install openpyxl
# openpyxl Excel .xlsx files read karne ke liye use hota hai.

# Man Lo Tumhre Pass Dusri shet hai 
# Sheet Name Se
df = pd.read_excel(
    "students.xlsx",
    sheet_name="Sheet1"
)

# yaaha sheet_name="Sheet1" ye battata hai ki kon si sheet import ho rahi hai 

# agr Apko sheet number se import karna hia toh 
# Sheet Number Se
df = pd.read_excel(
    "students.xlsx",
    sheet_name=0
)
#0 = First Sheet
#1 = Second Sheet


# agr Saari Sheets Read Karna
all_sheets = pd.read_excel(
    "students.xlsx",
    sheet_name=None
)
# Ye dictionary return karta hai.

# Common Parameters
# | Parameter    | Purpose                     |
# | ------------ | --------------------------- |
# | `sheet_name` | Kaunsi sheet read karni hai |
# | `usecols`    | Specific columns            |
# | `header`     | Header row                  |
# | `skiprows`   | Rows skip karna             |
# | `nrows`      | Kitni rows read karni hain  |
# | `na_values`  | Missing values define karna |


# csv VS excel me 
# Bas function alag hai, baaki bahut saare parameters same hote hain.

# Note : Excel file mein ek se zyada sheets (tabs) ho sakti hain. Jaise Excel ke niche tabs hote hain:
# Maan lo tumhari Excel file ka naam students.xlsx hai aur usme:

# Sheet1 → Student Data
# Sheet2 → Teacher Data
# Sheet3 → Course Data

# Read csv ke zcomparision me yaha thode kaam parameter hai but bahut simmlar hi hia eske jaise hi hai bhai 
