# drop(series + dataframe)
# ye Use hota hia jo apke rows ya col ko delete kar deta hai 

import pandas as pd 
import numpy as np
temp = pd.Series([10,2,3,16,45,78,10])
print(temp)

# chalo mujhekuch values ko delete karnahai 
# aap Drop use kar sakte ho 

ans = temp.drop(index=[0,6])
print(ans)

# ao dekhte hia data fram pe kase work karte hai 
students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]

    }
)

# mai Branch aur cgpa wale col ko drop karna chate hia 

temp = students.drop(columns=['branch','cgpa'])
print(temp)

# ab Dekhte hia row kaise delete kiye jate hia 
# mai Do rows ko delte karinga nitesh and adity index 0, 2 
# yaha Pe mai Col nahi 
ans = temp.drop(index=[0,6])
print(ans)

# esko karne se kuch nahi bass main change ho jate hia 
students.drop(columns=['branch','cgpa'],inplace=True)


# ye bhi ek tarika hai 
students.drop(columns=['branch','cgpa'],inplace=True)