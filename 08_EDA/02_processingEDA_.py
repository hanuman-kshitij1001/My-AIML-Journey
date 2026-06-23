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







#2-Steps of doing Univariate Analysis on Categorical columns

# Descriptive Statistics: Compute the frequency distribution of the categories in the column.
#                         This will give a general understanding of the distribution of the categories and
#                         their relative frequencies.

# Visualizations: Create visualizations to explore the distribution of the categories.
#                 Some common visualizations for categorical data include count plots and pie charts.
#                 These visualizations provide a visual representation of the distribution of the categories and
#                 can help identify any patterns or anomalies in the data.

# Missing Values: Check for missing values in the data and decide how to handle them. 
#                 Missing values can be imputed or excluded from the analysis, 
#                 depending on the research question and the data set.

# Conclusion:     Summarize the findings of the EDA and make decisions about how to proceed with further analysis.



# Note Sabse Pahel Toh Pahechna Sikho Ki Kon Kon se cat col hai 


# Lets Start with Survived Column
# conclusion :
            # Parent-child and SiblingSpouse cols can be merged to form a new col call family_size
            # Create a new col called is_alone


servive = train['Survived'].value_counts()
print(servive)
train['Survived'].value_counts().plot(kind='bar')
plt.show()

# Ye Kya hai : ye Hai Pie Chart jo ki Survived col ke liye hai
train['Survived'].value_counts().plot(kind='pie', autopct='%1.1f%%')
# autopct='%1.1f%%' Eska use hai ki ye percentage ko show karega pie chart me
plt.show()



#3- Steps of doing Bivariate Analysis Matlb do col ka Ek sath analysis karna hai

# Select 2 cols
# Understand type of relationship

#1-  Numerical - Numerical
#    a. You can plot graphs like scatterplot(regression plots), 2D histplot, 2D KDEplots
#    b. b. Check correlation coefficent to check linear relationship

# Numerical - Categorical - create visualizations that compare the distribution of 
#                           the numerical data across different categories of the categorical data.
#   a. You can plot graphs like barplot, boxplot, kdeplot violinplot even scatterplots

# Categorical - Categorical
# a. You can create cross-tabulations or contingency tables that show the distribution of values in one categorical column,
#    grouped by the values in the other categorical column.
# b. You can plots like heatmap, stacked barplots, treemaps

# Write your conclusions  ?





#4- Now we will move to feature engineering and feature selection


# feature engineering on fare column
train[[train['sibsp'] == 8]] 