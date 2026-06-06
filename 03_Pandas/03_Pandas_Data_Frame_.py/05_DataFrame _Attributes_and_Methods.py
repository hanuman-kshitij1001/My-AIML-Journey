# DataFrame Attributes and Methods
import pandas as pd
movies = pd.read_csv("03_Pandas/03_Pandas_Data_Frame_.py/02_Data_set_IPL_.csv")
ipl = pd.read_csv("03_Pandas/03_Pandas_Data_Frame_.py/03_Data_Set_movies_.csv")
student_data = [  # Esme 
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]

a = pd.DataFrame(student_data, columns=['iq','marks', 'package'])
print(a)

#1 movies.shape
a = ipl.shape
print(a)
b = movies.shape
print(b)

#2: # dtypes
a = movies.dtypes
b = ipl.dtypes
print(a, b)

#3: index 
a = movies.index
b = ipl.index
print(a, b)

# columns
a = movies.columns
b = ipl.columns
print(a, b)


# # values
a = movies.values
print(a)


## head and tail
a = movies.head(2)
b = movies.tail(2)
print(a, b)


## sample : ye Random Matches Select Karta hai bass data ka idea deta hai 
a = ipl.sample(5)
print(a)


## info: Ye apko Ek High Level Imnfo deta hai Bahut tarah ka infor ek sath deta hai 
# Imp Hai Bhahut
a = movies.info()
print(a)
b = ipl.info()


## describe Ye Mathmaticall Sumarray Deta hai jitne bhi numarical hai wo Detect karke Show kardeta hai , shirf Numrical col hi dikha Deta hai 
a = movies.describe()
b = ipl.describe()
print(a)
print(b)


# # isnull: ye batata hai ki apke data ke andhar null values hai ya nahi 
a = movies.isnull()  # jaha Pe apko False Dikhai De raha hai Samjh jaoa waha missising value nahi hai 
print(a)


b = movies.isnull().sum() #ye Kya KArega Haar col me jitne bhi missing val honge usse add kar denga 
print(b)


# # duplicated ye batata hai ki dublicates values hai kya toh ye check karta hai 
a = movies.duplicated()
print(a)   # yaha Bhi true ka matlb hia wo duplicate hua hai 

b = movies.duplicated().sum() # ye Bata Deta hai Ki Uss row Me Kitne Dup hai 
print(b)


# rename Ye apke Data Frame Ka Col ka Name ko rename Kar deta hai
# student_dict = {
student_dict = {
    'name':['nitish','ankit','rupesh','rishabh','amit','ankita'],
    'iq':[100,90,120,80,0,0],
    'marks':[80,70,100,50,0,0],
    'package':[10,7,14,2,0,0]
}
df = pd.DataFrame(student_dict)
df.rename(columns={'marks':'percent','package':'lpa'}, inplace=True)
print(df)


# Toh Jab Bhi Data Ke sath Khelna Ye sare function Chala Ke dekh lena Jab Bhi data Import karo usspe works karne se pahele 
