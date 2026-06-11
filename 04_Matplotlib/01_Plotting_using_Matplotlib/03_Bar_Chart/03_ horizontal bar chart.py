import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

children = [10,20,40,10,30]
colors = ['red','blue','green','yellow','pink']

plt.barh(colors,children,color='black')
plt.show()