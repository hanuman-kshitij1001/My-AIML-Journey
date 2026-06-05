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


import matplotlib.pyplot as plt
# Ex:1
# jaise sie  Ko Kissi Ne Bol Day By day Maine kitne Subscriber gain Kiye Uska Graph Ploat karo KAise KAre 
# Step 1: Mai Sabse Pahle  Series Ke Upper ploat function  lagayenge 
print(subs.plot())
plt.show()


#Ex:2 kin actors ne kiss traha ki movies bnaia hai 
print(movies.value_counts().head(20))
# valuecount esliye Usse kiya Ki Ye value Count karega . haed kyu usse kiye ye shirf head se 20 actir hi denga pura value nahi 
# ab Mai Espe Plot function Call karunga grap banane ke liye 
# ye kaam Mai Upper wale code me Direct bhi kar sakta tha 
movies.value_counts().head(20).plot(kind="bar")
# kind bar ka Matlb hia Graph hamra Bar chart me ban ke ayega kind ka matlb kaise banan hai 
# last me haam Call Kar denge Theek hai 
plt.show()

# chalo pia chart banate hia 
movies.value_counts().head(20).plot(kind="pie")
plt.show()


# AI 
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z)
plt.show()