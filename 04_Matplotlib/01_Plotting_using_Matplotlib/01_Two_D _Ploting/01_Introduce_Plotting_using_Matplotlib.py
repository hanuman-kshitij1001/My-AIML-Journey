# Haam yaha Pe Sikhne Wale hai ki Data Ko Graph Me kaise Plot karte hai 
# Hamesa Data Ko Graphs Me Plote Karne ke liye mujhe Essi Lib Ki jarurat padhti hai 
# Esse hame Data Ka Visulization Bahut acche de banaya jata hai 
# Yah Haam Log 3 Important Lib Padhne wale hai 
#1- Matploatlib
#2- seborn 
#3- ploatli
#4- tablu

# aj Haam Yha Shirf Matplot ke bare me hi padhne wale hai 
# So Matploat lib is Mother of All Visulation lib in python 
# Baki Ki Jo Lib hai Wo Eske hi upper banae hai 
# Esliye Eska Understanding Acche Se hona Jaruri hia THeek hai na 


# Aaj Ke Session Me Haam Log 5 alag types Ke Graph Ko Ploat karna Sikhne Wale hia 
#1- 2 d Plaot
#2- scatter ploat
#3- bar chart
#4- histogram 
#5- pia chart
# Ye esse Chart hai Ye aap Puri Journey Me bahut usse karoge Done 


# ab Yaha Samjhne Wali baat ye hai Ki 
#    Type data types: 
#1 - Numarical Data
#2 - Categorical Data : Jaha Pe apke Data Me Groups hote hai bcz there are cat in the Data
# Note Ye Jana Bahut imp hai ki aap kon se data ke Sath Deal kar rahe ho 
# Begneer ki Sabse badi problem Ki Kiss Type Ke Data Ke sath ki type ka graph ploat karna chahiye ?
# Wo jaane ke liye Apko Hamesha Pata hona Chaiye Ki
# 1- Data Numarical hai Ya Cat hai Theek Ye clearity Ye rakhna Hota hai 
# 2- Agr ap ek Single Col ke upper graph ploat kar rahe Hote ho usse Haam Univerte Analysis Bola Jata Hai agr aap ek Sath Do col ke Upper graph ploat karte ho toh use bi varent analysis bola jata hai , agr aap 3 col ya usse Jada sath me graph ploat kar rahe hote ho toh usko Multi varient analysis bola jata hai 

# to ye Dono Knownolge Hona Chaiye Kissi bhi Data Pe Move Karne Se pahele Theek ha Na 

# Aaj Ki Class Ke liye Jitni bhi Libiray Hai Wo Dowlode Karna Honga Lib Name mai Likh deta hun jo jo yaha pe Usse Hone Wali hai Done 
# Total 4 lib haam Import kar rahe hai 

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