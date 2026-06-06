# Eske Bahut tarike hai 
# Agr apko Data frame banna hia Toh Akko 2-D list ki Jarurat Padegi 
# chalo Isse List se banate hia 

# using lists
import pandas as pd
student_data = [  # Esme 
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]

a = pd.DataFrame(student_data, columns=['iq','marks', 'package'])
print(a)


#Ex:2 
data = {
    "Name": ["Amit", "Rahul", "Sneha"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)
print(df)



# using dicts : 
student_dict = {
    'name':['nitish','ankit','rupesh','rishabh','amit','ankita'],
    'iq':[100,90,120,80,0,0],
    'marks':[80,70,100,50,0,0],
    'package':[10,7,14,2,0,0]
}

df = pd.DataFrame(student_dict)
print(df)

# Ab Haam Read csv Se karne wale hai theek hai na 
movies = pd.read_csv("03_Pandas/03_Pandas_Data_Frame_.py/02_Data_set_IPL_.csv")
print(movies)
ipl = pd.read_csv("03_Pandas/03_Pandas_Data_Frame_.py/03_Data_Set_movies_.csv")
print(ipl)