# Histogram ek Univariate Plot hai.

# Use Kiya Jata Hai:
# 1. Numerical Data Ki Distribution Dekhne Ke Liye
# 2. Data Kis Range Me Jyada Hai Ye Dekhne Ke Liye
# 3. Frequency Count Karne Ke Liye
# 4. Skewness Aur Outliers Samajhne Ke Liye


# Key Points :
# Univariate Analysis
# Numerical col
# Use case - Frequency Count


# import the library

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1: DataSet
batsman = pd.read_csv("04_Matplotlib/01_Plotting_using_Matplotlib/My_Data_Set/01_batsman_season_record.csv")

#2: Data set 
batter = pd.read_csv("04_Matplotlib/01_Plotting_using_Matplotlib/My_Data_Set/02_batter.csv")

#3: Dataset:
big_array = pd.read_csv("04_Matplotlib/01_Plotting_using_Matplotlib/My_Data_Set/03_big-array.npy")

#4: DataSet
four_sixes  = pd.read_csv("04_Matplotlib/01_Plotting_using_Matplotlib/My_Data_Set/04_fours-sixes.csv")

#5: DataSet
gayle = pd.read_csv("04_Matplotlib/01_Plotting_using_Matplotlib/My_Data_Set/05_gayle-175.csv")

#6: DataSet
sharma_k = pd.read_csv("04_Matplotlib/01_Plotting_using_Matplotlib/My_Data_Set/06_sharma-kohli.csv")

#7: DataSet
vk = pd.read_csv("04_Matplotlib/01_Plotting_using_Matplotlib/My_Data_Set/07_vk.csv")