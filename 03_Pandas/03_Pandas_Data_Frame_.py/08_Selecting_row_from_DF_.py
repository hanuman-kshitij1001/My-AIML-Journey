# Selecting rows from a DataFrame Esme Do Cheeze Sikhni hai
# 1:  iloc - searches using index positions
# 2:  loc - searches using index labels

import pandas as pd
ipl = pd.read_csv("03_Pandas/03_Pandas_Data_Frame_.py/02_Data_set_IPL_.csv")
movies = pd.read_csv("03_Pandas/03_Pandas_Data_Frame_.py/03_Data_Set_movies_.csv")
student_data = [  
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
student_dict = {
    'name':['nitish','ankit','rupesh','rishabh','amit','ankita'],
    'iq':[100,90,120,80,0,0],
    'marks':[80,70,100,50,0,0],
    'package':[10,7,14,2,0,0]
}
students1  = pd.DataFrame(student_data, columns=['iq','marks', 'package'])
students2 = pd.DataFrame(student_dict)
students2.set_index('name', inplace=True)
print(students2)



# Single Row Fetching
print()
print(movies.iloc[1])

# fetching multiple ros using iloc
print(movies.iloc[0:5])
# fancy indexing bhi usse kari ja sakti hai yaha pe
print(movies.iloc[[0,4,5]])


# # loc
students2.loc['nitish']
students2.loc['nitish':'rishabh':2]
students2.loc[['nitish','ankita','rupesh']]
students2.iloc[[0,3,4]]



