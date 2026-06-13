# 2. Matrix Plot
#  . Heatmap
#  . Clustermap

#Heat Map : plots a Rectangual data as a color - enclosed matrix

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

tips = sns.load_dataset('tips')
# Ye Yaha Pe Jo Data Mil Raha hia Ye Hota hai Long Data 
# Esse Chaote Data Me Convert karne ke liye yaha use Kiya jata hai pivort table
# Pivot ke baad (Wide Format) 
# Isi format ko Heatmap bahut easily visualize kar sakta hai.

gap = px.data.gapminder()
temp_df = gap.pivot(index='country',columns='year',values='lifeExp')


# axes level function
plt.figure(figsize=(15,15))
sns.heatmap(temp_df)
plt.show()



# annot : Esse Kya Honga Number bhi plot hone lagta hai done 
temp_df = gap[gap['continent'] == 'Europe'].pivot(index='country',columns='year',values='lifeExp')

plt.figure(figsize=(15,15))
sns.heatmap(temp_df,annot=True,linewidth=0.5, cmap='summer')
plt.show()