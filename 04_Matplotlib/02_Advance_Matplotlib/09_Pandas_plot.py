import pandas as pd
iris = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/01_iris.csv")
batter = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/02_batter.csv")
batsman_session = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/03_batsman_season_record.csv")
ipl = pd.read_csv("04_Matplotlib/02_Advance_Matplotlib/All_dataSet/04_IPL_Ball_by_Ball_2008_2022.csv")



# yaha haam Kya Pdhne Wale Hia Ki Hamne Padas Se Plot function se graph toh ploat kar liya 
# tha but hamne kabhi bhi achee Se pandas Ploat padha Nahi
#  Toh Wahi haam Yaha Padnne Wale hai 

#Plot function ko aap Ese Samjh sakte ho ki pandas ek Bahut acchi lib hia 
# Matploblib bhi Ek Acchi Hi Lib hai 
# What If Haam Pandas me Ek Feature add kar de ki pandas me ek function ko call karke Haam Matplot likh ke graph Ko Ploat kar paye 
# That is the Whole Idea Of plot 
# So Ploat is A function of pandas Using Which plot you can plot graphs of  matlopb function inside a pandas 
# Plot Function Series ke upper aur D-F dono pe kaam karta hai 

# Chalo Dekhte hai plot use # on a series
import pandas as pd
# Ye bhai Inculde Karna Padhta hai 
import matplotlib.pyplot as plt

s = pd.Series([1,2,3,4,5,6,7])
s.plot(kind = 'line')

plt.show()   # Graph screen par dikhayega

#Note :  can be used on a dataframe as well

# Sabse Pahel Mai Seaborn aka restro wala data pe kaam karunga 

import seaborn as sns
df = tips = sns.load_dataset('tips')
df = tips['size'] = tips['size'] * 100
print(df)

# Ab Eska Graph bhi bana Lete hai 
tips.plot(kind='scatter', x = 'total_bill', y='tip')
plt.show()

# Ab  yaha Bhi wo sari Cheeze Use Kar sakte ho 
tips.plot(kind='scatter', x = 'total_bill', y='tip', title='Graph', c='red', marker='*', figsize=(10, 8), s='size', cmap='viridis')
plt.show()
# Dekha Pandas ne Sab Kuch Sara Wahi Ka wahi plot me hi de diya 


# line ploat:
# line ploat:
stocks = pd.read_csv("https://raw.githubusercontent.com/m-mehdi/pandas_tutorials/main/weekly_stocks.csv")
stocks["MSFT"].plot(kind ='line')
plt.show()

# 3 line Ka Ploating karte hai 
stocks.plot(kind='line')
plt.show()

# ab Bologe arey Dates Nahi A Rahe hia 
stocks.plot(kind='line', x='Date')
plt.show()

# agr apko 3 Line bass 2 Lines hi Chahiye toh 

stocks[['Date', 'MSFT', 'FB']].plot(kind='line', x='Date')
plt.show()


# let me Show  u Bar chart wala Graph 
# bar chart -> single -> horizontal -> multiple
# using tips
#tips.plot(kind='bar', x='sex', y='total_bill') Ye kaam nahi Kar raha hai But Niche Wala Chal  jayega 
tips.groupby('sex')['total_bill'].mean().plot(kind='bar')
plt.show()
# arey yaah Baar chart nahi bana 
# Chalo Esse mai Dusre Data Set pe Kar ke Dikhta hun 

batsman_session['2015'].plot(kind='bar', x='X-axis', y='Y-axis')
plt.show()

#Ex1:
batsman_session.plot(kind='bar')
plt.show()

#Ex2:
batsman_session.plot(kind='bar', stacked=True)
plt.show()

# Same Working Histo gram 
stocks.plot(kind = 'hist')
plt.show()

# ye 3 No Ka De raha Hai Agr apko 2 Ka Dena hai toh yaha Wo bhi Kar sakte hai 
# ya bins Me Divide karna hai TOh bhi 
stocks[['MSFT','FB']].plot(kind='hist',bins=40)
plt.show()


# Same With pia chart 
# pie -> single and multiple
# Ye mere Pass EK Data set hai 
df = pd.DataFrame(
    {
        'batsman':['Dhawan','Rohit','Kohli','SKY','Pandya','Pant'],
        'match1':[120,90,35,45,12,10],
        'match2':[0,1,123,130,34,45],
        'match3':[50,24,145,45,10,90]
    }
)
df['match1'].plot(kind='pie',labels=df['batsman'].values,autopct='%0.1f%%')
plt.show()


# multiple pie charts
df[['match1','match2','match3']].plot(kind='pie',subplots=True,figsize=(15,8))
plt.show()



# multiple separate graphs together
# using stocks
stocks.plot(kind='line',subplots=True)
plt.show()


# on multiindex dataframes
# using tips
tips.pivot_table(index=['day','time'],columns=['sex','smoker'],values='total_bill',aggfunc='mean').plot(kind='pie',subplots=True,figsize=(20,10))
plt.show()