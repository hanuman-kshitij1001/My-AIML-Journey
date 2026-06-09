# Merge Esse wo Log Jada ache samjh jayenge Jo SQL me joing karkhe hai 
# Wahi same Feature pandas me yaha diya gaya hai 


import pandas as pd
import numpy as np
nov = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/04_Data_Set_reg-month1.csv")
dec = pd.read_csv("03_Pandas/06_Marg_joining_Conct_/All Data Sets/05_Data_Set_reg-month2.csv")


# There  are four types of join 
# 1: inner join
# 2: left join
# 3: right join
# 4: outer join

# join apko kya karna hai Do data Frame ya do Table ko join karna hai 
# Lekin on the basis of same columns 
# kyu Eski jarurat padi 
# jaise man lo mere pass Student bolke df hai usme unka sara detail mere samne hai 
# Fhir mere pass ek regs bol ke data fram  jaha maine nov aur dec ke sare data ko jod ke ek df banaya hai 
# ab Let say koi es data ko dekh raha hai aur dekhta hia ki student id 23 ne coures id 1 me enro kiya , st id 15 ne  course me enrol kiya 
# Toh usne question puch ki ek kam karo ess data ko thoda aur improve kar do yaha ek col add kar do jo bhi student hai ye 23 uska name yaha display hona chahiye 
# Ab aap Agr baith ke socho kaise tum student bring karoge here ? 
# bahot simple hai 
# ye Jo reg wala col hai esko aap join kar donge 'student wale col ke sath kiss cheez ke basis pe joing honga 
# there is one common col in both of the data frame that is reg me students id hai aur aap students me jao toh waha bhi student id hai 
# ap Student id wale col ke basis pe in dono col ko join kar sakte ho 

