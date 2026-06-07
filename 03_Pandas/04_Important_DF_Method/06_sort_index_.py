# sort_index(series and dataframe)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
marks1 = pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14]
],columns=['iq','marks','package'])
ipl = pd.read_csv("03_Pandas/04_Important_DF_Method/02_Data_set_IPL_.csv")
movies = pd.read_csv("03_Pandas/04_Important_DF_Method/03_Data_Set_movies_.csv")
health = pd.read_csv("03_Pandas/04_Important_DF_Method/04_DataSet_Health.csv")
batsman = pd.read_csv("03_Pandas/04_Important_DF_Method/06_dataSet_batsman_runs_ipl.csv")


marks2 = {
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}

marks_series = pd.Series(marks2)  # Ye Apke Index ko Sort kar deta hai  yaha Mai Sabse pahele series pe dekh leta hun 
b = marks_series.sort_index(ascending=False)
print(marks_series)
print(b)

# yaha Movies wale data frame ko sort karunga from basis of index
# automatically kya honga jo data index sabse bada honga wo sabse upper a jayega
print(movies.sort_index(ascending=False))