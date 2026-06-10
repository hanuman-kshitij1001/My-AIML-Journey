# Timestamp Object
# Time stamps reference particular moments in time (e.g., Oct 24th, 2022 at 7:00pm)
# kabhi particular instance of time ko aap timestamp bula sakte ho 
# aur pandas ne apko ek alag datatype diya hai usse time stamp ko store karne ke liye usse hi haam 
# timestamp name hia uska 

# sabse aap ko ye janna honga ki aap kaise ek time stamp bana sakte ho 
# Step1:
# pd.Timestamp() esse call karna hota hai aur eske andhar ek string pass kar sakte ho jaise aaj ka data 
# hamesha yad rakharakha apko 
# YY / M / DD es formate me dena chahiye agr nahi bhi donge toh bhi ye samjha dar hai amjh jayega theek 

import pandas as pd
pd.Timestamp('2023/1/5')  #Output: Timestamp('2023-01-05 00:00:00')

type(pd.Timestamp('2023/1/5') )

# variations
pd.Timestamp('2023-1-5') # ye bhi likho toh bhi chaega 
pd.Timestamp('2023, 1, 5') # ye bhi chalega 

# only year
pd.Timestamp('2023')  # Timestamp('2023-01-01 00:00:00')


# using text
pd.Timestamp('5th January 2023')

# providing time also
pd.Timestamp('5th January 2023 9:21AM')


# AM and PM
# Am Donge toh AM me Ayega Pm donge toh 24 me ayega 

# yaha haam python se date time python ka utha rahe hai 
# using datetime.datetime object
# Ye date time hai python abhi tak uper ho haam padh rahe the wo pandas ka date tha 
import datetime as dt
x = pd.Timestamp(dt.datetime(2023,1,5,9,21,56))
print(x)
# fetching attributes
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)

# fayada kya hai time stamp bannane ka 


print()
# ye Python ka hai 
import pandas as pd
from datetime import datetime
# Abhi ka time
now = pd.Timestamp(datetime.now())
print(now)
# Output: 2024-01-15 14:30:25.123456

# Alag alag nikaalo
print("Saal    :", now.year)
print("Mahina  :", now.month)
print("Din     :", now.day)
print("Ghanta  :", now.hour)
print("Minute  :", now.minute)
print("Second  :", now.second)
print("Weekday :", now.day_name())  # Monday, Tuesday etc

# why separate objects to handle data and time when python already has datetime functionality?

# syntax wise datetime is very convenient
# But the performance takes a hit while working with huge data. List vs Numpy Array
# The weaknesses of Python's datetime format inspired the NumPy team to add a set of native time series data type to NumPy.
# The datetime64 dtype encodes dates as 64-bit integers, and thus allows arrays of dates to be represented very compactly.


print()
import numpy as np
date = np.array('2015-07-04', dtype=np.datetime64)
print(date)
print(date + np.arange(12))

# Because of the uniform type in NumPy datetime64 arrays, this type of operation can be accomplished much more quickly than if we were working directly with Python's datetime objects, especially as arrays get large
# Pandas Timestamp object combines the ease-of-use of python datetime with the efficient storage and vectorized interface of numpy.datetime64
# From a group of these Timestamp objects, Pandas can construct a DatetimeIndex that can be used to index data in a Series or DataFrame