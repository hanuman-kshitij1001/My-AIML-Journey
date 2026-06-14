#Plotting Pairwise Relationship (PairGrid Vs Pairplot)
# Esme Kya Hota hai ki :
# Ye Pair Waise Relation Ship Plot karta hia 
# Ye Kaam Ka Grph Hia Esse Future me BAhut kaam ayega 
# Esse irir ke data pe karte 
# Toh Pair ye automatically detect kar leta hai ki apke table me kitne Numbariacl col hai theek 
# aur fhie pair by pair apke sare numarical col ke becch me wo graph ko plot kar denaga 




import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
iris = px.data.iris()
sns.pairplot(iris)

# Esse Thoda Rang biranga Banna hia Toh Kya karna honga Ki hue kp species de dena honga 
sns.pairplot(iris,hue='species')



# Jite bhai numarical col honge unke utni hi wo grid bana lenga apne aap 

# ab Essi Ka Ek Baap hota hai pairgrid 
# pair ploat hamesha Pair grid Se banta hai 

# pair grid 
g = sns.PairGrid(data=iris)
# g.map
g.map(sns.scatterplot)
plt.show()  # Esse Kya honga sara ka Sara Scatter plot hi bana denga Done 

# map_diag -> map_offdiag

# Ye Wo Hai jo Hamne Sabse Pahele Plot kiya tha theek hai na 
g = sns.PairGrid(data=iris)
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
plt.show()
# Aba Bologe Kya Fayeda Hua Toh 
# Sabse pahlee Aap yaha pe hue Parameter add kar sakte ho 

# yaha Pe Jue Add kar raha hun waise hn ye ap pair plot me bhi kar sakte the 
g = sns.PairGrid(data=iris, hue='species')
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
plt.show()

# Asli benifit ye hia apke pass freedom  hia aap kuch bhi plot kar sakte ho 
# Jaise Kal ko aap Bol sakte ho ki apko hist plot nahi chahiye mujhe voilent chahiye 

g = sns.PairGrid(data=iris, hue='species')
g.map_diag(sns.violinplot)
g.map_offdiag(sns.scatterplot)
plt.show()

# Chalo Ab mai Box Plot bhi bana deta hun 
g = sns.PairGrid(data=iris, hue='species')
g.map_diag(sns.boxplot)
g.map_offdiag(sns.scatterplot)
plt.show()



# Chalo Ab mai Box Plot bhi bana deta hun aur scatter ko hata ke hist plot bana dete 2d hest plot 
g = sns.PairGrid(data=iris, hue='species')
g.map_diag(sns.boxplot)
g.map_offdiag(sns.scatterplot)
plt.show()


# Chalo Ab mai Box Plot bhi bana deta hun aur scatter ko hata ke hist plot bana dete 2d hest plot 
g = sns.PairGrid(data=iris, hue='species')
g.map_diag(sns.boxplot)
g.map_offdiag(sns.histplot)
plt.show()



# Chalo Ab mai Box Plot bhi bana deta hun aur scatter ko hata ke ke badle 2d kde plot chahiye 
g = sns.PairGrid(data=iris, hue='species')
g.map_diag(sns.boxplot)
g.map_offdiag(sns.kdeplot)
plt.show()


# map_diag -> map_upper -> map_lower
# Matlb mai yaha pe Upper niche ka bass data print kar sakta hun theek hai na 
g = sns.PairGrid(data=iris,hue='species')
g.map_diag(sns.histplot)
g.map_upper(sns.kdeplot)
g.map_lower(sns.scatterplot)


# vars
g = sns.PairGrid(data=iris,hue='species',vars=['sepal_width','petal_width'])
g.map_diag(sns.histplot)
g.map_upper(sns.kdeplot)
g.map_lower(sns.scatterplot)