# kdeplot
# ye bhhi apko data ka distribution hi batata hia but ye histogram ki tarah bins bana ke nahi batata hai 
# Ye Fuction ko use karke apka jo data hia usse smaooter kar deta hai 
# Aur smooter karne ke wajha se jo apko curve milta hai usse KD plot bola jata hai theek hai 
# Eske Maths Me nahi ja rahe hai abhi ye Padhenge jab Statics Padhenge toh theek hai na 
# Rather than using discrete bins, a KDE plot smooths the observations with a Gaussian kernel, producing a continuous density estimate

# I can Take The Tips Data set Bro Done Ok Ok 

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# paheli baat Kabhi jab bhi nai files Use karo Toh Usse Load karna maat bhulna bhai 
tips = sns.load_dataset('tips')

sns.kdeplot(data=tips,x='total_bill')
plt.show()

# Note ye Jada use Hota hai As Compar to Histplot 

# u Can Plot the Same Plot using dis plot also 
sns.displot(data=tips,x='total_bill',kind='kde')
plt.show()


# yaha Pe bhi hue prameter Exsiting 
#hue -> fill
sns.displot(data=tips,x='total_bill',kind='kde',hue='sex',fill=True,height=10,aspect=2)
plt.show()