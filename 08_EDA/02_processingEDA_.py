# Step1 : import all The Files 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

train = pd.read_csv("08_EDA/DatSets/train.csv")
test = pd.read_csv("08_EDA/DatSets/test.csv")

print(train.head())
print(test.head())

# Note : # Remember it is an iterative process
# Column Types
#1- Numerical - Age,Fare,PassengerId
#2- Categorical - Survived, Pclass, Sex, SibSp, Parch,Embarked
#3- Mixed - Name, Ticket, Cabin

# Let Start univariate analysis for age column
# Age:
# Conclision : 
df = train["Age"].describe()
# print(df)
# sns.histplot(train["Age"], kde=True)
# plt.show() 

# df['Age'].plot(kind='kde')
# plt.show()

# df['Age'].plot(kind='box')
# plt.show()

fare = train['Fare'].describe()
print(fare)

sns.histplot(train["Fare"], kde=True)
# plt.show()

skew = train['Fare'].skew()
print("Skewness of Fare column is : ", skew)

fare = train['Fare'].plot(kind='box')
print(fare)

Total_fare = train[train['Fare'] > 250]
print("Total number of passengers having fare greater than 250 is : ", Total_fare.shape[0])

# So Toh Jo Conculsion hai :
#1- The data is highly(positively) skewed
#2- Fare col actually contains the group fare and not the individual fare(This migth be and issue)
#3- We need to create a new col called individual fare

