# value_counts
# sort_values
# rank
# sort index
# set index
# rename index -> rename
# reset index
# unique & nunique
# isnull/notnull/hasnans
# dropna
# fillna
# drop_duplicates
# drop
# apply
# isin
# corr
# nlargest -> nsmallest
# insert
# copy

# Each one of them is Important 
# Agr Ye 20+ function Acche se use karna a gaye toh app data set bahut acche se usse aur maupulate kar paoge 


import numpy as np
import pandas as pd
marks = pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14]
],columns=['iq','marks','package'])


# Method 1: value_counts(series and dataframe)
# Har Unique Item ki Freq Ka Count nikal ke deta hai 
# JAise haam marks Wale Pe Chalene Wale hai 
a = marks.value_counts()  # Ye Pure Rows Ka Freq Count nikal Raha hai 
                          # Ye bahut usse full nahi rahta hai Pure data frame p elagta hia esliye But hn ye series me Kaam KArta hai 
print(a)