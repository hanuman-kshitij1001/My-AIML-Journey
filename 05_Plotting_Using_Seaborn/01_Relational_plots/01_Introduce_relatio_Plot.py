# 1. Relational Plot:
# . to see the statistical relation between 2 or more variables.
# . Bivariate Analysis

# Plots under this section
# . scatterplot
# . lineplot

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px    # Yemai Esliye Use kar raha hun Data Set Import karne ke liye 


# Mai Quicky import a data set which s present my seborn lib that is tips

tips = sns.load_dataset('tips')

# scatter plot -> axes level function
sns.scatterplot(data=tips, x='total_bill', y='tip')

# # relplot -> figure level -> square shape
sns.relplot(data=tips, x='total_bill', y='tip', kind='scatter')
# hamse Figure level Function Use karna 

# let See Hinden Parameter:
# relplot -> figure level -> square shape
sns.relplot(data=tips, x='total_bill', y='tip', kind='scatter',hue='sex',style='time',size='size')


# line plot
gap = px.data.gapminder()
temp_df = gap[gap['country'] == 'India']
temp_df

sns.lineplot(data=temp_df, x='year', y='lifeExp')

# Esse aap relplot se bhi karro
# using relpplot
sns.relplot(data=temp_df, x='year', y='lifeExp', kind='line')


# Parameter:
# 1-hue -> style
temp_df = gap[gap['country'].isin(['India','Brazil','Germany'])]
temp_df

# ab Mai 3 no Ka line ploat karunga 
sns.relplot(kind='line', data=temp_df, x='year', y='lifeExp', hue='country')

#ab Chaho esme aur bhi Cheeze dekha sakte ho 
sns.relplot(kind='line', data=temp_df, x='year', y='lifeExp', hue='country', style='continent')

# ye Bahot Intreseting Cheez Hai Called 
# facet plot()
sns.relplot(data=tips, x='total_bill', y='tip', kind='scatter',hue='sex')

# Kissi Ek Particul col ke upper Multil plot bana sakte ho 
sns.relplot(data=tips, x='total_bill', y='tip', kind='scatter', col='smoker', row='sex')

#ab mai Yaha Days Daal Du Toh Usme 8 Category Hia Toh Jada Graph Banega 
sns.relplot(data=tips, x='total_bill', y='tip', kind='scatter', col='smoker', row='days')


# Ye Same kaam Ap Line Plot ke sath Bhi Kar sakte The agr kind ko line kar ton 

#Note: Its Wok only fig level function only 
# facet plot -> figure level function -> work with relplot
# it will not work with scatterplot and lineplot
sns.relplot(data=tips, x='total_bill', y='tip', kind='line', col='sex', row='day')
# this is The Proof 


# # col wrap: kya karta pane aap se col ko set kar sakte ho 
# Ye Kya 

sns.relplot(data=gap, x='lifeExp', y='gdpPercap', kind='scatter', col='year', col_wrap=3)