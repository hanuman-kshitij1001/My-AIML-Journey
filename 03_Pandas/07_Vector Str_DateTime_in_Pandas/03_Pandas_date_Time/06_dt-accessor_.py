# dt accessor
# Accessor object for datetimelike properties of the Series values.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('03_Pandas/07_Vector Str_DateTime_in_Pandas/03_Pandas_date_Time/01_DS_expense_data.csv')

# ✅ Sirf Date column convert karo
df['Date'] = pd.to_datetime(df['Date'])
print(df.dtypes)



# Plot
plt.plot(df['Date'], df['INR'])
plt.show()


# day name wise bar chart/month wise bar chart
df['day_name'] = df['Date'].dt.day_name()
df.groupby('day_name')['INR'].mean().plot(kind='bar')
plt.show()



df.groupby('month_name')['INR'].sum().plot(kind='bar')
plt.show()