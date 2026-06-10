# ye ek range me dates ka values genrate karta hai 

import pandas as pd
# generate daily dates in a given range
pd.date_range(start='2023/1/5',end='2023/2/28',freq='3D')
# start se end tak sare date genrate kar denga done 



# alternate days in a given range
pd.date_range(start='2023/1/5',end='2023/2/28',freq='3D')
# 3D matlb 3 din ka atlernate genration 



# B -> business days
pd.date_range(start='2023/1/5',end='2023/2/28',freq='B')
# B = M TO F days S, S automatically hata denga 

# W -> one week per day
# Har Hafte ka Ek din hi de rahahai 
pd.date_range(start='2023/1/5',end='2023/2/28',freq='W-THU')

# H -> Hourly data(factor)
# Ye Haar Gnate ka time stap genratekarega from start se end tak 
pd.date_range(start='2023/1/5',end='2023/2/28',freq='6H')


# M -> Month end
pd.date_range(start='2023/1/5',end='2023/2/28',freq='M')


# MS -> Month start
pd.date_range(start='2023/1/5',end='2023/2/28',freq='MS')


# A -> Year end
pd.date_range(start='2023/1/5',end='2030/2/28',freq='A')


# using periods(number of results)
pd.date_range(start='2023/1/5',periods=25,freq='M')