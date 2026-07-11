#   Series methods
#   head() aur tail() Pandas Series (aur DataFrame) ke sabse useful methods me se hain.

#1: Head and Tail :
#Ye Data Ka PReview Deta hai 
# head() : Series ke starting ke rows dikhata hai.

import pandas as pd

s = pd.Series([10,20,30,40,50,60,70])

print(s.head())
# Note : Default me pehle 5 values dikhata hai.

# Agar specific number chahiye:Toh Use 
# head(n)
print(s.head(3))


# tail() Series ke last ke rows dikhata hai.
print(s.tail())
# Note ye Bhi Last ke Default me last 5 values dikhata hai.
# tail(n)
print(s.tail(2))


# Real-life use
# Maan lo tumne CSV load ki:
subs = pd.read_csv("03_Pandas/02_Pandas_Series/09_DataSet_subs.csv")
# Maan Lo es Puri file me 1000+ rows ho sakti hain.
# Agar tum:
print(subs.head())
#karoge, to file ke shuru ke 5 records dekh loge.
# Aur
print(subs.tail())
# karoge, to last ke 5 records dekh loge.

# Isse quickly check kar sakte ho ki data sahi load hua ya nahi.



# 2: Bhai Pandas me sample() ka kaam hai random rows/values uthana.
import pandas as pd
s = pd.Series([10,20,30,40,50,60,70])
print(s.sample())

# Example 2: Multiple random values
print(s.sample(3))
# print(s.sample(3))

#Example 3: Same random result har baar
print(s.sample(3, random_state=42))
# random_state seed set karta hai, isliye har baar same output aayega.


# Real-world use
# Maan lo tumhare paas 10,000 subscribers ka data hai:
subs = pd.read_csv("03_Pandas/02_Pandas_Series/08_DataSet_kohli_ipl.csv")
# Agar tum dekhna chahte ho ki data kaisa lag raha hai bina poori file khole:
print(subs.sample(5))
# To 5 random rows mil jayengi.
#            Difference yaad rakho
#         Method	       Kaam
#         head()	       Shuru ki rows
#         tail()	       Last ki rows
#         sample()	       Random rows


# 3:Value Count ; yee kya karta hai ki data Me Value ki Jo Freq Hai Wo Count karke bata hai 

s = pd.Series(["A", "B", "A", "C", "B", "A"])
print(s.value_counts())

s = pd.Series([10, 20, 10, 30, 20, 10])
print(s.value_counts())

# Tere IPL ya Bollywood dataset me
vk = pd.read_csv("03_Pandas/02_Pandas_Series/08_DataSet_kohli_ipl.csv")
print(vk.value_counts())


# 4: Sort value: Sabhi Values Ko Sort kar deta hai 
# sort_values() ka kaam hai values ko sort (ascending ya descending order) me arrange karna.
s = pd.Series([50, 10, 30, 20, 40])
print(s.sort_values())
# Dhyan do:
# Values sort ho gayi hain.
# Original index wahi reh gaya hai.


# Descending order
print(s.sort_values(ascending=False))

# method 
# vk.sort_values(ascending=False).head(1).values[0]
# Step 1: sort_values(ascending=False)
# Step2 : .head(1) = Sirf pehli row lega.
# Step 3: .values  >> Series ko NumPy array me convert kar deta hai.
# Step 4: [0] >...>  Array ka pehla element nikal lo.



# 5:  sort_index -> inplace -> movies
# sort_index() ka matlab hai: Index ko sort karo, values ko nahi.
movies = pd.read_csv("03_Pandas/02_Pandas_Series/07_DataSet_bollywood.csv")
movies.sort_index(inplace=True)
print(movies)    # Ye Permanent Change Hia inplace Change Kar rahe Hai haam theek hai na 
print(type(movies))
