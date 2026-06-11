import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

tips = sns.load_dataset('tips')
print(tips)
# yaha pe aap Notice karo thoh Do numariacl col hai 

plt.scatter(tips['total_bill'], tips['tip'])
plt.show()

# agr tum chaho toh ek ek Chheeze aur add kar sakte ho thats is wo kitne longo ke sath aya taha

plt.scatter(tips['total_bill'], tips['tip'], s= tips['size'])
# dot bada Dikhega Agr Jada Longon ke sath aya Honga , Chot ikhega Agr Kaam Longon Ke Sath Aya Honga
plt.show()


# Chalo Enko Color bhi dete hai 
plt.scatter(tips['total_bill'], tips['tip'], s= tips['size'], color='red')
plt.show()

# Mai Ap ko yaha Ye Batna Chahta Hun ki 
# aap  chalo aap bina scater function ko call kiye bhi scatter ka graph ploat kar sakt ho kaise 
# # scatterplot using plt.plot   > using "plt.plot" se 
plt.plot(tips['total_bill'],tips['tip'],'o')
plt.show()
# 'o' Ye Use Kiya ho gaya 
# yaad Rakhna This Technique is Faster Bro instead of scatter theek 


# plt.plot vs plt.scatter   ..  # plt.plot > plt.scatter