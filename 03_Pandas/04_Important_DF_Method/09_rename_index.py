# rename(dataframe) -> index


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
# rename ka Kaam Hota hia colomn ko rename karana theek hai na 
# maine yaha movei ke name ko hi index baana diya hai 
movies.set_index('title_x',inplace=True)

# yaha Kuch kuch ho toh raha hai pata nahi kya ho raha hai 
# bass yaha mai dekh raha hun col ka name badal diya gaya hai 
movies.rename(columns={'imdb_id':'imdb','poster_path':'link'},inplace=True)


# yaha Kya Hua index change kiya hamne 
movies.rename(index={'Uri: The Surgical Strike':'Uri','Battalion 609':'Battalion'})