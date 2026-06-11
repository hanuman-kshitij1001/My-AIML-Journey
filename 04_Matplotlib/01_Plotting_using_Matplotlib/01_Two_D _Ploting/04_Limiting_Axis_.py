

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# limiting axes
# Limiting Axes ka matlab hota hai graph me X-axis ya Y-axis ki visible range ko control karna.
price = [48000,54000,57000,49000,47000,45000,4500000]
year = [2015,2016,2017,2018,2019,2020,2021]

plt.plot(year,price)
plt.show()


# Ex2:
plt.plot(year,price)
plt.ylim(0,75000)
plt.xlim(2017,2019)
plt.show()