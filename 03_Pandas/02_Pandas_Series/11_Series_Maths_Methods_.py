import pandas as pd
vk = pd.read_csv("03_Pandas/02_Pandas_Series/08_DataSet_kohli_ipl.csv")
movies = pd.read_csv("03_Pandas/02_Pandas_Series/07_DataSet_bollywood.csv")
sub = pd.read_csv("03_Pandas/02_Pandas_Series/09_DataSet_subs.csv")


#1:  count : total number items Count karke bata deta hai but ye missing value ko count nahi karta  hai but size ye bhi kar deta hai 
a = vk.count()
print(a)
print()

# Out-put :
# match_no    215
# runs        215

#2: sum or  product 
b = sub.sum()
c = sub.prod()
print(b)
print(c)

#3: mean / median / mode / std / var
m = sub.mean()
n = vk.median()
l = movies.mode()
p = sub.std()
q = sub.var()
print()
print(m)
print(n)
print(l)
print(p)
print(q)


#4: min / max
print()
w = sub.min()
y = sub.max()
print("Minimum ", w)
print("Maximum", y)


#5: discribe  == ye jo pura apne ek ek karke kara hai esse ye ek list me de deta hai 
g = vk.describe()
print()
print(g)