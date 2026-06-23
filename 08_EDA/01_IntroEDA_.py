# EDA = Exploratory Data Analysis
# Machine Learning aur Data Science me EDA ka matlab hota hai data ko explore karna aur samajhna before model training.
# "Data ko dekhna, samajhna, clean karna, aur uske patterns identify karna" = EDA
# EDA kyu karte hain?

# Agar bina EDA ke model bana diya to:

#1- Missing values reh sakti hain
#2- Wrong data types ho sakte hain
#3- Outliers model kharab kar sakte hain
#4- Features ke relationships samajh nahi aayenge

#Isliye Data Science ka rule hai:
#    Data Collection
#        ↓
#       EDA
#        ↓
#   Data Cleaning
#        ↓
#   Feature Engineering
#        ↓
#   Model Building
#        ↓ 
#   Evaluation



# Why do EDA
#1- Model building
#2- Analysis and reporting
#3- Validate assumptions
#4- Handling missing values
#5- feature engineering
#6- detecting outliers


# Column Types
#1- Numerical - Age,Fare,PassengerId
#2- Categorical - Survived, Pclass, Sex, SibSp, Parch,Embarked
#3- Mixed - Name, Ticket, Cabin

# Basically yaha Pe Hama Ye Samjha Sare Hai Ki Kaise Univarient karte hia Bhai Done 
# Univariate Analysis
# Univariate analysis focuses on analyzing each feature in the dataset independently. Chalo Jante Hia Univariate Analysis ke Benefits:
# 1- Distribution analysis: The distribution of each feature is examined to identify its shape,
#    central tendency, and dispersion.
# 2- Identifying potential issues: Univariate analysis helps in identifying potential problems with the data
#    such as outliers, skewness, and missing values


#The shape of a data distribution refers to its overall pattern or form as it is
#represented on a graph. Some common shapes of data distributions include:
#1- Normal Distribution: A symmetrical and bell-shaped distribution where the mean, median, and mode 
#   are equal and the majority of the data falls in the middle of the distribution with gradually decreasing frequencies towards the tails.
#2- Skewed Distribution: A distribution that is not symmetrical, with one tail being longer than the other.
#   It can be either positively skewed (right-skewed) or negatively skewed (left-skewed).
#3- Bimodal Distribution: A distribution with two peaks or modes.
#4- Uniform Distribution: A distribution where all values have an equal chance of occurring.

# Note:
# The shape of the data distribution is important in identifying the presence of outliers,
# skewness, and the type of statistical tests and models that can be used for further analysis.

### Steps of doing Univariate Analysis on Numerical columns
# 1-Descriptive Statistic:  Compute basic summary statistics for the column, such as mean, median, mode, standard deviation, range, and quartiles. These statistics give a general understanding of the distribution of the data and can help identify skewness or outliers.
# 2-Visualization:  Create visualizations to explore the distribution of the data. Some common visualizations for numerical data include histograms, box plots, and density plots. These visualizations provide a visual representation of the distribution of the data and can help identify skewness an outliers.
# 3-Identifying Outlier:    Identify and examine any outliers in the data. Outliers can be identified using visualizations. It is important to determine whether the outliers are due to measurement errors, data entry errors, or legitimate differences in the data, and to decide whether to include or exclude them from the analysis.
# 4-Skewnes:    Check for skewness in the data and consider transforming the data or using robust statistical methods that are less sensitive to skewness, if necessary.
# 5-Conclusion:  Summarize the findings of the EDA and make decisions about how to proceed with further analysis.
