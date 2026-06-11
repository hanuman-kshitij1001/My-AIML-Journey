#Scatter Plot me har observation ek dot (point) ke form me dikhaya jata hai.
# Use hota hai:
# ✅ Bivariate Analysis (2 numerical columns)
# ✅ Relationship check karne ke liye
# ✅ Correlation dekhne ke liye
# ✅ Outliers identify karne ke liye


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


# Again three Important Things
# Bivariate Analysis
# numerical vs numerical ke upar hi plot hi honga 
# Use case - Finding correlation