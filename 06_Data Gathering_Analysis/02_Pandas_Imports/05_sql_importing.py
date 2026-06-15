# SQL (Structured Query Language)

# Ab hum dekhenge ki databases ke saath kaise kaam karte hain.

# SQL ek language hai jiska use databases ko create, manage aur query
# karne ke liye kiya jata hai.

# Companies ka adhiktar data databases mein store hota hai,
# isliye SQL Data Analysis ka ek bahut important skill hai.

# Database -> Tables ka collection
# Table -> Rows aur Columns ka collection

# Example Students Table

# +----+---------+-----+
# | ID | Name    | Age |
# +----+---------+-----+
# | 1  | Kshitij | 20  |
# | 2  | Rahul   | 21  |
# +----+---------+-----+

# Common SQL Commands

# SELECT -> Data fetch karna
# INSERT -> Data add karna
# UPDATE -> Data modify karna
# DELETE -> Data remove karna

# Example Queries

# SELECT * FROM students

# SELECT Name, Age FROM students

# SELECT * FROM students
# WHERE Age > 20

# Pandas mein SQL data read karne ke liye:

# import sqlite3
# import pandas as pd

# conn = sqlite3.connect("college.db")

# df = pd.read_sql(
#     "SELECT * FROM students",
#     conn
# )

# SQL ka use:
# 1. Databases se data fetch karne mein
# 2. Data filtering aur analysis mein
# 3. Reports banane mein
# 4. Business Intelligence mein

# Important:
# Data Analyst ki job mein Pandas aur SQL dono saath-saath use hote hain.

# One Line:
# SQL ek language hai jiska use databases mein stored data ko access,
# manage aur analyze karne ke liye kiya jata hai.




# Step 1: Database Se Connect Karo
# SQLite example:
import sqlite3
import pandas as pd

conn = sqlite3.connect("college.db")
# Yahan conn database se connection hai.

# Step 2: SQL Query Chalao Aur DataFrame Banao
df = pd.read_sql(
    "SELECT * FROM students",
    conn
)
print(df)
# Ab SQL table Pandas DataFrame ban gaya.

# Real Industry Flow
# MySQL / PostgreSQL / SQL Server
#                 ↓
#            SQL Query
#                 ↓
#         Pandas DataFrame
#                 ↓
#       Cleaning + Analysis
#                 ↓
#       Visualization / ML