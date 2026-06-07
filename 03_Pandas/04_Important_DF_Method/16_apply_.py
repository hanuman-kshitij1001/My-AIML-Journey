# apply(series + dataframe)


import pandas as pd
import numpy as np
temp = pd.Series([10,20,30,40,50])
print(temp)

# Chalo ab Apko kissi ne bol diya bhai apko har value ka sigmoid banna hai 

def sigmoid(value):
    return 1/1+np.exp(-value)

a = temp.apply(sigmoid)
print(a)


points_df = pd.DataFrame(
    {
        '1st point':[(3,4),(-6,5),(0,0),(-10,1),(4,5)],
        '2nd point':[(-3,4),(0,0),(2,2),(10,10),(1,1)]
    }
)
 # ese esliye bana hai ki mai ab df pe kaam karne wale hai 
 # do col hai aur dono col me do - do points diye hai 

# ek row me do point unka Eculidain dis nikalo aur usse new col me bhejna hia 
# row ke upper bhi app apply chal akte ho 

def euclidean(row):
    pt_A = row['1st point']
    pt_B = row['2nd point']
    return ((pt_A[0]-pt_B[0])**2 + (pt_A[1]-pt_B[1])**2)**0.5
points_df.apply(euclidean, axis = 1) # axis == 1 se kya matlb hia ap row bhej rahe ho 

points_df['distance'] = points_df.apply(euclidean,axis=1)
print(points_df)