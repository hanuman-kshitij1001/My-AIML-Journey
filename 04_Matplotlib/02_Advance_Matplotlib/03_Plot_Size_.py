# Plot size ; Graph Ke Size ko Increase decrese kiya ja sakta hai 


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

iris = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/01_iris.csv")


#size badhne ke liye likho:
plt.figure(figsize=(15,10))
# So yaha pe 15 will Become The widdth of the graph 
# and 7 is The Hieght 



plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'], c= iris['Species'], cmap='jet', aplha='0')
plt.xlabel('Sepal Length')
plt.ylabel('PetalLenght')
plt.colorbar()
plt.show()