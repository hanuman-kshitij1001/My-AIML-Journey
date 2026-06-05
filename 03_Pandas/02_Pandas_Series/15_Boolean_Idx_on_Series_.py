# Find no of 50's and 100's scored by kohli

import pandas as pd 

vk = pd.read_csv("03_Pandas/02_Pandas_Series/08_DataSet_kohli_ipl.csv")
movies = pd.read_csv("03_Pandas/02_Pandas_Series/07_DataSet_bollywood.csv")
subs = pd.read_csv("03_Pandas/02_Pandas_Series/09_DataSet_subs.csv")
x = pd.Series([12,13,14,35,46,57,58,79,9])
marks = [82,96,85,45,65,87,100]
subjects = ['maths', 'english', 'Hindi', 'Science', 'History', 'UPSC', 'Physics']
marks = {
    'maths' : 67,
    'English':85,
    'Hindi':89,
    'Physics':100,
    "Advance Backchodi":1000
}
marks_series = pd.Series(marks)

#Q1:Find no of 50's and 100's scored by kohli Matlb Matlb Kitne Matches Me banai Virat ne 
a = vk[vk >= 50].size
print(a)


#Q2: # find number of ducks; Duck Matlb Virat ne kitne 0 banai 
vk[vk == 0].size



#Q3: Count number of day when I had more than 200 subs a day
subs[subs > 200].size


#Q4: # find actors who have done more than 20 movies
num_movies = movies.value_counts()
num_movies[num_movies > 20]