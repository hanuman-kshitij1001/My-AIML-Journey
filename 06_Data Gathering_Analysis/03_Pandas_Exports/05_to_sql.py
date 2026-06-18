# to_sql() thoda alag hai CSV, Excel, JSON se.
# Wahan tum file bana rahe the.
df = []
df.to_csv()
df.to_excel()
df.to_json()

# Lekin to_sql() me DataFrame ka data database table me save hota hai.

# Why to_sql()?
# Maan lo tumhare paas DataFrame hai:  = df
# | Name    | Age |
# | ------- | --- |
# | Kshitij | 20  |
# | Rahul   | 21  |
# Aur tum chahte ho ye data database ke table me save ho jaye:
# Students Table:
# | Name    | Age |
# | ------- | --- |
# | Kshitij | 20  |
# | Rahul   | 21  |
# To use karte hain: df.to_sql()

# Flow

# DataFrame
#     ↓
# to_sql()
#     ↓
# Database Table


#Basic Syntax

df.to_sql(
    name='students',
    con=connection
)

# Yahan:
# name → table ka naam
# con → database connection


# Sabse Easy Example (SQLite)  :   SQLite Python ke saath hi aata hai.
import pandas as pd
import sqlite3
# ab DataFrame

df = pd.Dataframe({
    'Name':['Kshitij', 'Ayush'],
    'Age' : [20, 21]
})

# Database Connection

conn = sqlite3.connect("student.db")

# DataFrame → SQL Table
df.to_sql(
    name='students',
    con=conn,
    if_exists='replace',
    index=False
)

conn.close()


# SIR
# import pymysql
# from sqlalchemy import create_engine

# engine create_engine("mysql+pymysql://root:@localhost/ipl")
# #{root}:{password}@{url}/{database}
# df.to_sql('ipl_delivery', con engine, if_exists 'append')

# temp_df.to_sql('batsman_runs', con = engine, if_exists = 'append')
# temp_df2