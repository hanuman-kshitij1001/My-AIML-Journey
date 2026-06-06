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


# Selecting both rows and cols:

a = movies.iloc[0:3,0:3]
print(a)

# maine Yaha 0 se 2 row Col ko hi fetch kiya hai kaise 
b = movies.loc[0:2,'title_x':'poster_path']