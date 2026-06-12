#3D Scatter Plots

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

iris = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/01_iris.csv")
batter = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/02_batter.csv")
batsman_session = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/03_batsman_season_record.csv")
ipl = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/04_IPL_Ball_by_Ball_2008_2022.csv")


# Esme haam Log 4 - types ke plots Sikhne Wale hai 
#1- Scatter ploat
#2- Line Plot
#3- Surface Plot 
#4- contour plots

# Basic Syntax 
fig = plt.figure()
ax = plt.subplot(projection='3d')
plt.show()

#1- Scatter ploat:
# 3-d Me plot karna matlb aap 3 quanties ke beech Ploting kar rahe jaise haam 2-d me do ke bich me karte hai wais ehi yaah 3 ke bech me kane wala hai
 
fig = plt.figure()
ax = plt.subplot(projection='3d')
ax.scatter3D(batter['runs'],batter['avg'],batter['strike_rate'],marker='+')
ax.set_title('IPL batsman analysis')
ax.set_xlabel('Runs')
ax.set_ylabel('Avg')
ax.set_zlabel('SR')
plt.show()



# Yah Kya Hua Ao Batate hai 
#2- Line Ploat

x = [0,1,5,25]
y = [0,10,13,0]
z = [0,13,20,9]
fig = plt.figure()
ax = plt.subplot(projection='3d')
ax.scatter3D(x,y,z,s=[100,100,100,100])
ax.plot3D(x,y,z,color='red')
plt.show()


#3D Surface Plots
# Ye ML me Loss FUnction Hota hai Waha Uska Graph Ploat karn apadta hai Waha Ye kaam Ata hai 
# ab Kya karenge yaha Ek 3-D function x^2 and Y^2 ka Graph Ploat karenge theek hai na 

x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
xx, yy = np.meshgrid(x,y)
z = xx**2 + yy**2
z.shape
fig = plt.figure(figsize=(12,8))
ax = plt.subplot(projection='3d')
p = ax.plot_surface(xx,yy,z,cmap='viridis')
fig.colorbar(p)
plt.show()

#Ex3: 

z = np.sin(xx) + np.cos(yy)
fig = plt.figure(figsize=(12,8))
ax = plt.subplot(projection='3d')
p = ax.plot_surface(xx,yy,z,cmap='viridis')
fig.colorbar(p)
plt.show()


#4; Contour Plots 
# Actually ye Mere 3d Ko 2-D me Convert kar Deta hai 
# Theek hai na Hanji Done 

fig = plt.figure(figsize=(12,8))
ax = plt.subplot()
p = ax.contour(xx,yy,z,cmap='viridis')
fig.colorbar(p)
plt.show()

#ex 2:
fig = plt.figure(figsize=(12,8))
ax = plt.subplot()
p = ax.contour(xx,yy,z,cmap='viridis')
fig.colorbar(p)
plt.show()


#Ex:3
z = np.sin(xx) + np.cos(yy)
fig = plt.figure(figsize=(12,8))
ax = plt.subplot()
p = ax.contourf(xx,yy,z,cmap='viridis')
fig.colorbar(p)