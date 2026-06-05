import pandas as pd

country = ['India','America','USA', 'Japan', 'Austria']
# aap Ab Es List agr Series banana chahte ho toh kya karn ahonga apko 
print(pd.Series(country))
# Pandas Ke Andhr ek Function Hota hSeries Ka Theek Hai Na 
# Output:
# 0      India
# 1    America
# 2        USA
# 3      Japan
# 4    Austria
# dtype: object
# Out me hamesha Index Aur Value Dono Ho print Hoti Hai Hamesha 
# Index and Uski Value

# Chalo Haam Kuch aur Type Ka Series Bante hia 
# Integer ka 

runs = [13,52,6,37,48]
print(pd.Series(runs))

# Abhi Tak hamne dekha ki Haame Kudh Se by default index Mil raha tha But 
# Agr Haam Chahe toh Khud ka bhi index Name Provide kar sakte hia kaise Chal dekhte hia 

marks = [82,96,85,45,65,87,100]
subjects = ['maths', 'english', 'Hindi', 'Science', 'History', 'UPSC', 'Physics']

# Ab Aap Ek Series banayenge k Jo Marks Hai Wo Value Bana Ke Dikhai De aur subject hamre index honge Theek 
output = pd.Series(marks, index=subjects)
print(output)

# Output:
# maths       82
# english     96
# Hindi       85
# Science     45
# History     65
# UPSC        87
# Physics    100
# dtype: int64

# Agr aap Chaho To aap apne Series object ko name De sakte ho jisko Future me bula sakte ho usse kar sakte hai 
# mai YAhi Marks Aur Subject le leta hun 

Reffence = pd.Series(marks, index=subjects, name='Kshitij Tiwari Na,e Se Reffrence')
print(Reffence)
#Out-put:
# maths       82
# english     96
# Hindi       85
# Science     45
# History     65
# UPSC        87
# Physics    100
# Name: Kshitij Tiwari Na,e Se Reffrence, dtype: int64
# Ye Name Bolke Jo Additiona Imformation Hai Yahi Reffence hai 

