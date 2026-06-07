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


#1: astype
ipl.info()

ipl['ID'] = ipl['ID'].astype('int32')
ipl.info()


# ipl['Season'] = ipl['Season'].astype('category')
ipl['Team1'] = ipl['Team1'].astype('category')
ipl['Team2'] = ipl['Team2'].astype('category')


ipl.info()