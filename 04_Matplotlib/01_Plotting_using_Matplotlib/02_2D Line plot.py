import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Ye Apke Graph Ke Style ke Liye Usse kiya jata hai 
plt.style.use('default')
# By Default Hoti hia 

print(plt.style.available)
# ye sari style dikha deta hai 



# yaah maine Bass Esse Use Kiya Esse Mai Ek Chala Raha hun For Output Showing 
# plt.style.use('tableau-colorblind10')
plt.plot([1,2,3,4],[10,20,15,30], label='A')
plt.plot([1,2,3,4],[30,15,25,10], label='B')
plt.plot([1,2,3,4],[5,10,20,25], label='C')
plt.legend()
plt.show()



# Our Topic 

# 2-D Line Kab Usse kiya jata Hai 
# Ye Use Kiya Jata hai For
# 1-Bivariate Analysis - Do col ke upper
# 2-categorical -> numerical and numerical -> numerical
# 3-Use case - Time series data
plt.style.use('default')
plt.show()



# plotting a simple function
price =  [48000,54000,57000,49000,47000,45000]
year =  [2015,2016,2017,2018,2019,2020]
plt.plot(year, price)
plt.show()


## from a pandas dataframe
#6: DataSet
sharma_k = pd.read_csv("04_Matplotlib/01_Plotting_using_Matplotlib/My_Data_Set/06_sharma-kohli.csv")

plt.plot(sharma_k['index'], sharma_k['V Kohli'])
plt.show()


# Ek Sath Ek Graph pe Multiple Ploating Kar raha hun 
# plotting multiple plots

plt.plot(sharma_k['index'],sharma_k['V Kohli'])
plt.plot(sharma_k['index'],sharma_k['RG Sharma'])
plt.show()


# Chalo Ab Batna Sikte hai Ki X axis pe kya hai Aur Y axis pe kya hai Etc 
# Eska Syntax hota hai 
plt.title('Rohit Sharma Vs Virat Kohli Career Comparison')
plt.plot(sharma_k['index'],sharma_k['V Kohli'])
plt.plot(sharma_k['index'],sharma_k['RG Sharma'])
plt.show()
# Ab Jab Chaoge toh Upper ye Title ayega 


# Agr Mujhe X ya Y axis Pe Title Dalna hai toh mai Uske liye bhi kuch cheeze batadeta hun 
plt.xlabel("Meri X Axis Hai ye ")
plt.ylabel("Meri Y axis hai ye ")
plt.plot(sharma_k['index'],sharma_k['V Kohli'])
plt.plot(sharma_k['index'],sharma_k['RG Sharma'])
plt.show()


# Mai Esse Oroginal Tarike Se bhi Kar deta hun Matlb Taext ko 

plt.title('Rohit Sharma Vs Virat Kohli Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')
plt.plot(sharma_k['index'],sharma_k['V Kohli'])
plt.plot(sharma_k['index'],sharma_k['RG Sharma'])
plt.show()
# ab ye Pura Sab Ka Comination ho gaya hai



# colors(hex) and line(width and style) and marker(size)
# Eska Kya Matlb hai :Chalo batate Hai 
# Essa kyu Hua Vk Ka Line Ka Color blue Aya Aur Rohit ka Yello What if Agr mujhe Kuch Chahiye Toh To ye Wahi Karta hai 
# Ki aap Apni Marzi Se Color Badal Sakte ho 

# Chalo Mai VK ko Green dena hai Uske Liye Ek Hiden Parameter hotahai Color Bolke 
plt.plot(sharma_k['index'],sharma_k['V Kohli'], color="green")

#Chalo R ko Black Dete hia 
plt.plot(sharma_k['index'],sharma_k['RG Sharma'], color='black')
plt.show()



# ab Yaha Solid Line Ban rahi hai esse change kare kya Chalo 
plt.plot(sharma_k['index'],sharma_k['V Kohli'],color='#D9F10F',linestyle='solid',linewidth=3)
plt.plot(sharma_k['index'],sharma_k['RG Sharma'],color='#FC00D6',linestyle='dashdot',linewidth=2)

plt.title('Rohit Sharma Vs Virat Kohli Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')

# ab yaha Ham Points ko mark De diya hun 
plt.plot(sharma_k['index'],sharma_k['V Kohli'],color='#D9F10F',linestyle='solid',linewidth=3,marker='D',markersize=10)
plt.plot(sharma_k['index'],sharma_k['RG Sharma'],color='#FC00D6',linestyle='dashdot',linewidth=2,marker='o')

plt.title('Rohit Sharma Vs Virat Kohli Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')