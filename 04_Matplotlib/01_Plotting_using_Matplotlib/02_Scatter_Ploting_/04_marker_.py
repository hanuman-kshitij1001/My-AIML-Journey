# marker ka matlab hai graph ke har data point par kaunsa symbol dikhana hai.

#Normal line plot:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data

year = [2015, 2016, 2017, 2018, 2019, 2020]
price = [48000, 54000, 57000, 49000, 47000, 45000]

plt.plot(year, price)
# Output:  ────────────
# Sirf line dikhegi.



# Marker lagao
plt.plot(year, price, marker='o')
# Output:
# o────o────o────o


# Common Markers

# 'o' -> Circle
# '+' -> Plus
# '*' -> Star
# 'x' -> Cross
# '.' -> Point
# 's' -> Square
# '^' -> Triangle Up
# 'v' -> Triangle Down
# 'D' -> Diamond



# Marker Size
#6: DataSet
sharma_k = pd.read_csv("04_Matplotlib/01_Plotting_using_Matplotlib/My_Data_Set/06_sharma-kohli.csv")
plt.plot(year, price,
         marker='o',
         markersize=10)


# Marker Color

plt.plot(year, price,
         marker='o',
         markerfacecolor='red')


# Example

plt.plot(sharma_k['index'],
         sharma_k['V Kohli'],
         marker='+')

plt.show()


# Summary

# linestyle  -> Line ka design
# color      -> Line ka color
# linewidth  -> Line ki thickness
# marker     -> Data Point ka symbol
# markersize -> Marker ka size