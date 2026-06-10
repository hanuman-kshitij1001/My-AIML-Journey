# DatetimeIndex Object
# A collection of pandas timestamp
# Ek Time Stamp ko time stamp bolte hai bahut sar time stams ke collection DatetimeIndex bolte hai 

#1: from strings
# Let me show you date time index kaise banta hia 

import pandas as pd
pd.DatetimeIndex(['2023/1/1','2022/1/1','2021/1/1'])  # yaha Maine EK List ke andhr dates bheji hai done

# Ap Eska Typpe bhi adekha sakte ho 
type(pd.DatetimeIndex(['2023/1/1','2022/1/1','2021/1/1']))

#2: # using python datetime object
# Yaha Haam Pythons ke Data time se create kar rahe hai
import datetime as dt
pd.DatetimeIndex([dt.datetime(2023,1,1),dt.datetime(2022,1,1),dt.datetime(2021,1,1)])

# using pd.timestamps
dt_index = pd.DatetimeIndex([pd.Timestamp(2023,1,1),pd.Timestamp(2022,1,1),pd.Timestamp(2021,1,1)])


#  using datatimeindex as series index
pd.Series([1,2,3],index=dt_index)