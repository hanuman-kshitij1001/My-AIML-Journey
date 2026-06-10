# What are vectorized operations
# Esko aap Har data setpe appy karoge jaha text honga Theek hia done 
# Bahut essay hai
# aap Pandas use karke string ke uper vectorize operation kar sakte ho \
# vercotrize opreation wo opreation hote hia jiss cheez ke upper ap opreation kar rahe hote ho wo ek vector hota hai 
# vector matlb set of things 
# Ex 1:
import pandas as pd
import numpy as np
a = np.array([1,2,3,4])
print(a)

# Question ye hia ki a*4 karu toh kya honga , apke array me jitne bhi element hai wo 4 se multi plye  ho jayenge 
# Now This Is The Example of Vectorize opreation 
# hua kya ki apke pass ek vector tha 1, 2, 3, 4 aray apne uspe ek single opreation chalaya lekin wo apke pure har elemet pe laga 
# essi Ko bola jata hai vectorize opration
# Matlb Ek baar mein poore array/column pe operation karna — element by element loop lagane ki zaroorat nahi!


import numpy as np

numbers = [1, 2, 3, 4, 5]

# ❌ Normal Loop — ek ek karke
result = []
for n in numbers:
    result.append(n * 2)
print(result)  # [2, 4, 6, 8, 10]


# ✅ Vectorization — ek saath sab pe
numbers = np.array([1, 2, 3, 4, 5])
result = numbers * 2
print(result)  # [2, 4, 6, 8, 10]


# Pandas mein Vectorization:
# ❌ Loop — slow
# for i in range(len(df)):
#     df['tip'][i] = df['tip'][i] * 2

# # ✅ Vectorized — fast
# df['tip'] = df['tip'] * 2


# Loop        →  1 ek ek student ka result check karo
# Vectorization →  Ek saath poori class ka result check karo

# ag haam Yahi Padhne  wale hai 
# haam padhege ki vectorize string opreation 
# apke Pass Ek column honga  usme bahut sare strings honge 
# Apko ek string opreation chalana Hai jo automaically apke haar row kw uppar apply hone lagega essi ko bola jata hai vectorize string opreation 


#pandas me VS methode esliye diye huye hai kyu ki jo apka python hai usme VS wala code ya v wala kaam etne acche se kaam nahi karte hia mai apko dikhta hun 
# man Lo mere pass ek string list hia 
# mujhe ye nikln hai ki kon kon se word c se start hote hai 


s = pd.Series(['cat','mat',None,'rat'])
[i.startswitch('c') for i in s]
# ess list me nin hone ke wajah se ye opreation nahi honga aur sahi bat hai  start string ke upper hota
# yahi sabse badi problem hai ki agr pke pass none ya missing data hai toh yaha ye kaakm ho nahi skata hai 
# Then There is  a second problem ye bahut slow bhi hai 

# thats why pandsa ne esse samjha aur eska solution nikal
# # becuse fast hone ka reson yahi hai ki pandas numpy pe baana hai aur numpy c se bana hua hai esliye ye spped c se a rahi hai 


s = pd.Series(['cat','mat',None,'rat'])
#srt = string accessor ye basically ejk add on function jab bhi usse karoge esse lagna padega 
s.strstartswitch('c')
# dekha ye handle kar liya pandas ne 