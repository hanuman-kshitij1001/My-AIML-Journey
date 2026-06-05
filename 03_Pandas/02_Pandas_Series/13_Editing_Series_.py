# Editing Series : 
# how Can We edit the item in series
# Abhi tak Haam Bass Read kar rahe the Ab Haam Edit karenge 
import pandas as pd 

vk = pd.read_csv("03_Pandas/02_Pandas_Series/08_DataSet_kohli_ipl.csv")
movies = pd.read_csv("03_Pandas/02_Pandas_Series/07_DataSet_bollywood.csv")
sub = pd.read_csv("03_Pandas/02_Pandas_Series/09_DataSet_subs.csv")
marks_series = pd.Series([85,63,98,75,69])

#1: using indexing:
print(marks_series)
marks_series[1] = 100
print(marks_series)


#2: what if an index does not exist
# marks_series['evs'] = 100
# this Code is Not through An error 
# If It Is Not Avlable Then New Item Can be Added Bro 
# If Is not avible it automatically created

#3:  slicing
#ye Sam ekaam Haam slicing me bhi kar sakte hai 
# runs_ser[2:4] = [100,100]
# runs_ser

# # fancy indexing ;
# Ye kaam Haam fancy indexing Series Me bhi kar sakte hai 
# runs_ser[[0,3,4]] = [0,0,0]
# runs_ser

# You Can Aslo Done it In Lables 
# using index label
# movies['2 States (2014 film)'] = 'Alia Bhatt'
# movies


# Note We Can Not use more in future 
