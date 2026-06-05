# coreration cofeciant 
# Ye bhi Imp Hia 
# Ye Mera -1 se 1 ke bech hota hai Ye number  hame ye batayega ki in Number ke Bich Corelation kitna hai 
# 1 corelation yaad hai na 
# 0 corelation 
#-1 coreetion

import numpy as np
salary = np.array([200000, 500000, 700000, 900000, 600000])
experience = np.array([1,3,2,4,2])
coree = np.corrcoef(salary, experience)
print(coree)