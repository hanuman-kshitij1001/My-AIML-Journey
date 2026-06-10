# Kay Padhoge yaha Pe Tum 
# actualy date time pandas me hadle kata karta dt wale data ko 
# Date aur Time ko ek special format mein store karna jisse hum usse easily manipulate kar sakein!
# Real world data mein date/time bahut common hai:
# 🛒 E-commerce    →  Order date, delivery date
# 🏦 Banking       →  Transaction time
# 📈 Stock Market  →  Price har minute
# 🏥 Hospital      →  Patient admit/discharge time
# ✈️ Flight        →  Departure, arrival time

df = []

# Problem — CSV mein date string me hoti hai:

# CSV se aane ke baad date ek simple string hoti hai
df['date'] = "2024-01-15"  # yeh sirf text hai!

# String se kuch calculate nahi kar sakte
df['date'] + 30  # ❌ Error!

# Solution — DateTime mein convert karo:

import pandas as pd
df['date'] = pd.to_datetime(df['date'])
# Ab calculate kar sakte ho!
df['date'] + pd.Timedelta(days=30)  # ✅ 30 din baad ki date

# DateTime se kya kya nikal sakte hain:
df['date'] = pd.to_datetime(df['date'])

df['year']    = df['date'].dt.year    # Saal
df['month']   = df['date'].dt.month   # Mahina
df['day']     = df['date'].dt.day     # Din
df['weekday'] = df['date'].dt.weekday # Somwar=0, Raviwar=6
df['hour']    = df['date'].dt.hour    # Ghanta


# Real Use Cases:
# 1. Do dates ka fark nikalna
df['days_taken'] = df['delivery_date'] - df['order_date']

# 2. Kisi month ki sales dekhna
january_sales = df[df['date'].dt.month == 1]

# 3. Weekend ki orders
weekends = df[df['date'].dt.weekday >= 5]

# 4. Ek saal ki data
df_2030 = df[df['date'].dt.year == 2030]




#DateTime Formats:
# Alag alag formats handle kar sakta hai
pd.to_datetime("2024-01-15")        # YYYY-MM-DD
pd.to_datetime("15/01/2024")        # DD/MM/YYYY
pd.to_datetime("January 15, 2024")  # Month DD, YYYY
pd.to_datetime("15-Jan-2024")       # DD-Mon-YYYY


# DateTime — Summary Table
# | Kaam                  | Code                          |
# |-----------------------|-------------------------------|
# | String → DateTime     | pd.to_datetime(df['col'])     |
# | Saal nikalna          | df['col'].dt.year             |
# | Mahina nikalna        | df['col'].dt.month            |
# | Din nikalna           | df['col'].dt.day              |
# | Do dates ka fark      | date2 - date1                 |
# | Month filter          | df[df['col'].dt.month == 1]   |
# | Year filter           | df[df['col'].dt.year == 2024] |
# | Weekend filter        | df[df['col'].dt.weekday >= 5] |
# | Ghanta nikalna        | df['col'].dt.hour             |



# aaj Ham Waise Yaha Do bject baanna bhi sikhnge 
# 1: Timestamp object
# 2: Datetimeindex object
