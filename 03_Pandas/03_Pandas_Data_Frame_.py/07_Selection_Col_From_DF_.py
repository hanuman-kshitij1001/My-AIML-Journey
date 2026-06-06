import pandas as pd
ipl = pd.read_csv("03_Pandas/03_Pandas_Data_Frame_.py/02_Data_set_IPL_.csv")
movies = pd.read_csv("03_Pandas/03_Pandas_Data_Frame_.py/03_Data_Set_movies_.csv")
student_data = [  # Esme 
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
students  = pd.DataFrame(student_data, columns=['iq','marks', 'package'])
movie = pd.DataFrame(movies)    #jarurat nahi hai bydefault ye data frame hi hai 
#1: single cols
# Agr Single Col Fetch karna hai Toh kaise karoge 
a = movie['title_x']
print(a)

# mai Nikal na Chata hun shir venu ka col 
b = ipl['Venue']
print(b)


# ab mai apko dikhta hun kaise Multiple col fetch arte hai 
# man Lo Hme 3 col nikalna hI a
# tile , actor , year of release 
# hm yaha fancy indexing use karenge

a = movie[['title_x','year_of_release','actors']]
print(a)

b = ipl[['Team1', 'Team2', 'WinningTeam']]
print(b)