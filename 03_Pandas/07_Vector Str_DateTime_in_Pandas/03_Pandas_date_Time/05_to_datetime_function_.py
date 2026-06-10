# to_datetime function
# converts an existing objects to pandas timestamp/datetimeindex object
# Bahit usse karne wale ho esse bhai sahab 

import pandas as pd

# simple series example

s = pd.Series(['2023/1/1','2022/1/1','2021/1/1'])
pd.to_datetime(s).dt.day_name()

# with errors
# to_datetime apply karte wqt eror a jate hia 
s = pd.Series(['2023/1/1','2022/1/1','2021/130/1'])
pd.to_datetime(s,errors='coerce').dt.month_name()
# '2021/130/1' jaise valid number nahi tha tohh "errors='coerce'" ye eese handle karta hai 


# chalo aab Data se karte hai 
df = pd.read_csv('03_Pandas/07_Vector Str_DateTime_in_Pandas/03_Pandas_date_Time/01_DS_expense_data.csv')
print(df.shape)
print(df.info())

# Esko karne se lya pata chala df abhi string me hai toh haam esppe date_time wali nahi run kar sakte hia esko mai convert karunga 

df['Date'] = pd.to_datetime(df['Date'])
print(type(df))

print(df.info())

# ab 
# a = df['Date'].dt.is_quarter_start
# print(a)

# ploat graph
import matplotlib.pyplot as plt
plt.plot(df['Date'],df['INR'])
plt.show()