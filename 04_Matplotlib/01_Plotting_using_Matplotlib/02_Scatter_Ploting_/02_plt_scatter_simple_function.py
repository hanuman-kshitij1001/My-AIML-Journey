
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# plt.scatter simple function
x = np.linspace(-10,10,50)
y = 10*x + 3 + np.random.randint(0,300,50)
plt.plot(x, y)
plt.show()


# But 
plt.scatter(x,y)
plt.show()