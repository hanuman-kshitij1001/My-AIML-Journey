# Clustermap : Ye kya hai  Ye bahut simliar hai heat map se ye apke data ke upper clustring karta hai matlb kya ha eska Simillar data ko ek Sath Lata hai 
# Matlb ki Same col ko sath le ayega Aur Diff ko alg le ja jayege theek hai na 
# Clustermap heatmap + hierarchical clustering hota hai.
# Ye rows aur columns ke beech similarity calculate karta hai aur phir similar rows/columns ko paas-paas arrange kar deta hai.

# Plot a matrix dataset as a hierarchically-clustered heatmap.

# This function requires scipy to be available.

# Ek Data Hai iris bolke Ye bahut hi famous data set hai haanji theek hai na 
# Chalo epe kaam karte hai theek hai na 

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

iris = px.data.iris()
print(iris)

# Load Data From sns 
iris = sns.load_dataset('iris')

# Ye Dikha Raha hai Ki Kon kon col apash me jada Simillar hai theek hai
sns.clustermap(iris.iloc[:,[0,1,2,3]])
plt.show()
# Esne Col ka View Change kar diya theek hai na 