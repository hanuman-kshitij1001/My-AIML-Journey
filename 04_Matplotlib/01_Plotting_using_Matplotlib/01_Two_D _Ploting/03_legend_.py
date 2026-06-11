import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sharma_k = pd.read_csv("04_Matplotlib/01_Plotting_using_Matplotlib/My_Data_Set/06_sharma-kohli.csv")

# ledgen Kya Karta hai ki 
# Legend graph ka label box hota hai jo batata hai ki kaunsi line kis cheez ko represent kar rahi hai.
# Example bina legend ke:
plt.plot([1,2,3,4],[10,20,15,30])
plt.plot([1,2,3,4],[30,15,25,10])
plt.show()

# Graph me 2 lines to dikhenge, lekin kaunsi line kya hai pata nahi chalega.


#Legend ke saath:

plt.plot([1,2,3,4],[10,20,15,30], label='Virat Kohli')
plt.plot([1,2,3,4],[30,15,25,10], label='Rohit Sharma')
plt.legend()
plt.show()

#Ab graph me ek chhota sa box aayega:

plt.plot(sharma_k['index'],sharma_k['V Kohli'],color="#F1970F",linestyle='solid',linewidth=3,marker='D',markersize=5,label='Virat')
plt.plot(sharma_k['index'],sharma_k['RG Sharma'],color="#00CEFC",linestyle='dashdot',linewidth=2,marker='o',label='Rohit')

plt.title('Rohit Sharma Vs Virat Kohli Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')
plt.legend(loc='upper left') # esse Wo Lable left - right hota hai 
plt.show()