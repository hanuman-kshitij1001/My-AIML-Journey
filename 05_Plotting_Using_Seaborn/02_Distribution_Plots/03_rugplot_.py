# rugplot: ye Utna use Full toh nahi hota hia but ye esa graph hai jisse ap support me bahut usse karte ho theek hai na 
# jaise Ek Plot Aap Bana Chuke Ho aur Addinatonal Plot as a information aap esska usse kar sakte ho theek hai na 
# Rug Plot ek bahut simple distribution plot hai jo data ke har observation ko ek chhoti line (tick mark) ke roop me axis par dikhata hai.

# Plot marginal distributions by drawing ticks along the x and y axes.
# This function is intended to complement other plots by showing the location of individual observations in an unobtrusive way.

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# paheli baat Kabhi jab bhi nai files Use karo Toh Usse Load karna maat bhulna bhai 
tips = sns.load_dataset('tips')

sns.kdeplot(data=tips,x='total_bill')
sns.rugplot(data=tips,x='total_bill')
plt.show() # Es Graph me Notice karna ki Niche X axis pe kuch Extra Dikh raha honga Wahi hai rug plot Done 


# Mai a tp or bill Dono ka graph banaunga That Called Bivarient 
# Bivariate histogram
# A bivariate histogram bins the data within rectangles that tile the plot 
# and then shows the count of observations within each rectangle with the fill color

# sns.histplot(data=tips, x='total_bill', y='tip')
sns.displot(data=tips, x='total_bill', y='tip',kind='hist')
plt.show()


# Bivariate Kdeplot
# a bivariate KDE plot smoothes the (x, y) observations with a 2D Gaussian
sns.kdeplot(data=tips, x='total_bill', y='tip')
plt.show()

# Yaha Ye Bhai Complte Hota hai 