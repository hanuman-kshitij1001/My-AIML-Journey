import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

iris = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/01_iris.csv")
# Ye Bahut Hi Famous Data Set Hai 


plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'])
plt.xlabel('Sepal Length')
plt.ylabel('PetalLenght')
plt.show()

# ab Esse Color Dete hai 
# eske liye apko Apne Col Ke Tag ko Koi Number Asign Karna honga Kaise klaroge 
iris['Species'] = iris['Species'].replace({'Iris-setosa':0,'Iris-versicolor':1,'Iris-virginica':2})
iris.sample(5)

# ab Jab Asign Ho gaye Toh Apko Yaha Ana HIa Aur  " c = iris['Species]"
plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'], c= iris['Species'])
plt.xlabel('Sepal Length')
plt.ylabel('PetalLenght')
plt.show()

# You can add a Color bar Fucntion
plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'], c= iris['Species'])
plt.xlabel('Sepal Length')
plt.ylabel('PetalLenght')
plt.colorbar()
plt.show()


# Ek aur parameter hota hai aplha Ye Dikhta hai ki Apke Graph Ka Opacity kitna honga 
plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'], c= iris['Species'], cmap='jet', aplha='0')
plt.xlabel('Sepal Length')
plt.ylabel('PetalLenght')
plt.colorbar()
plt.show()