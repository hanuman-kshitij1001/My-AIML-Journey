# Distribution Plots
# . used for univariate analysis
# . used to find out the distribution
# . Range of the observation
# . Central Tendency
# . is the data bimodal?
# . Are there outliers?

# Plots under distribution plot
#.  histplot
#.  kdeplot
#.  rugplot


# Lets Start With Hist plot 
# histogram hi Hist plots hai apka o data hai usme aap beens create karte ho 
# Bass Yahi hai 

# EssePlot karne ke liye simple ek fuction hota hai hist plot usse haam plot karte hia 

#figure Level -> displot
#axes level -> histplot -> kdeplot -> rugplot

# ploting univariate histogram 



import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# paheli baat Kabhi jab bhi nai files Use karo Toh Usse Load karna maat bhulna bhai 
tips = sns.load_dataset('tips')

sns.histplot(data=tips, x='total_bill')
plt.show()

# agr haam Esse Figure Level Pe Graph Banaye toh Kais banega 
sns.displot(data=tips, x='total_bill', kind='hist')
plt.show()

# bins parameter
sns.displot(data=tips, x='total_bill', kind='hist',bins=2)

# It’s also possible to visualize the distribution of a categorical variable using the logic of a histogram. 
# Discrete bins are automatically set for categorical variables
# Genrally aap Num pe hi karte ho Histogram Ko but aap Chaho toh Esse catagorical pe bhi kar sakte ho Done 
# YE not histogram ap esse count plot bolte hai 
# countplot
sns.displot(data=tips, x='day', kind='hist') 


# yaah Pe Bhi apke pass hue paramete hota hai 
# hue parameter
sns.displot(data=tips, x='tip', kind='hist',hue='sex')

# agr apko Ye Clear nahi dikh raha hai toh inhone eske liye ek para meter diye hai called Elements 
# element -> step
sns.displot(data=tips, x='tip', kind='hist',hue='sex',element='step')


# Note:
#  yaha Ye Data Etna famous nahi hai mai apko yaha pe famous data pe kaam kark dikhta hun that is titanic data set Theek hai na 
#  Ek important baat mai usse bhi yaha pe import kar sakta hun theek hai na
titanic = sns.load_dataset('titanic')

# Haam Kya Karba Chahte hia ki Age ka Histogramm Plot karege 
sns.displot(data=titanic, x='age', kind='hist',element='step',hue='sex')


# yaha pe bhi app fect aad kar sakte ho
# faceting using col and row -> not work on histplot function
sns.displot(data=tips, x='tip', kind='hist',col='sex',element='step')