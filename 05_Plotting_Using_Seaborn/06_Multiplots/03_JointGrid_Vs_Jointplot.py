# JointGrid Vs Jointplot
# ye Kya Karega 



import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
iris = px.data.iris()
tips = px.data.tips()


# Let me Show U joint plot kya karta hi 
sns.jointplot(data=tips,x='total_bill',y='tip')
# Since yaha ye do Num col hai 
# apko ek scatter plot ho jayega done 
# but at the same time joint plot kya karta hai ki apko apke dono ndivisula numarical col ke upper ye histo gram bhi plot karke deta hai 
plt.show()

# Ab Yaha Apke pass ABhut sare kind parameter bhi hote hia 
#1 kde
#2 hist
#3 reg Etc 
sns.jointplot(data=tips,x='total_bill',y='tip',kind='hist',hue='sex')
plt.show()

# ab yaha pe joint grid ka bhi opton hota hia 
g = sns.JointGrid(data=tips,x='total_bill',y='tip')
g.plot(sns.kdeplot,sns.violinplot)
plt.show()

# More Utility fuction 
# Agr Apko Ye dekhna hia Ki Built in seabor me kiten Data Set hia 
# get dataset names
sns.get_dataset_names()


# load dataset
# Matlb matb yaha haam ye dekh rahe hia ki kaise data set load hote hai 
sns.load_dataset('planets')
