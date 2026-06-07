# rank(series)
# ye Shirf Series par hi lagta hai df pe nahi 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
marks = pd.DataFrame([
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




print(batsman.head())
b = batsman['batting_rank'] = batsman['batsman_run'].rank(ascending=False)
print(b)
print(batsman.sort_values('batting_rank'))
