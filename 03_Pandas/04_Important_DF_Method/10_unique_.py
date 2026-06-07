# unique(series)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd





# apke ek particular series ya col ke andhr se ek particular sari unique nikal ke deta hai 
temp = pd.Series([1,1,2,2,3,3,4,4,5,5,np.nan,np.nan])
print(temp)
result = temp.unique()
print(result)

#  haam unquie Ka Len nikal Sakte hai
a = len(temp.unique())
print(a)

b = temp.nunique  
# jab Aap ye chalte ho toh wo nan ko count nahi karta hai 
# lekin Upar wala Denga Theek hai na 
print(b)