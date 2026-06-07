# reset_index(series + dataframe) -> drop parameter

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


batsman.reset_index()
print(batsman)

# # how to replace existing index without loosing

#1:
# batsman.reset_index().set_index('batting_rank')
# ye pata nahi kyu chal nahi raha hai withour lossing the col 
# replce karna hai col toh kya tarika hai pahle reset karo fhir usse set karo 
# Esse kya honga bina replcement ke Cheeze set ho jati hai 


marks2.reset_index()
print(marks2)