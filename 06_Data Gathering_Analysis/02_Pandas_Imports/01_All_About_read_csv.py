# How To Import data : Kaha Se Kaise kon - kon Se formate me done hai na ha 
# abhi Tak Haam read csv se data import karte the 
# aaj Haam Esse Aur detail Me Padhne Wale Theek 
# Pahleli baat toh ye samjho ki Data import karne ka matlb hai ki 
# CSV, Excel, SQL, JSON, etc. files ka Data python mein load karna that is called data import process 

# sabse pahle mai apko bata deta hun ki csv files hota kya hai 
# CSV ka full form hai Comma-Separated Values.
# Ye ek simple text file hoti hai jisme data rows aur columns ke form mein store kiya jata hai. Har column ko comma (,) se separate kiya jata hai.

# Example CSV File

# students.csv
# Name,Age,Marks
# Kshitij,20,85
# Rahul,21,90
# Priya,19,88


# CSV Kyu Use Hoti Hai?
# Lightweight hoti hai
# Excel, Python, R, SQL sab support karte hain
# Data sharing ke liye bahut common format hai
# Human-readable hoti hai (Notepad mein bhi khol sakte ho)

# 1. CSV File Import Karna (Sabse Common)
# abhi Haam Yaha Bass pd.reas_csv ki baat karne wale hai theek hai na hn ji 

1#  Cheez
import pandas as pd
df = pd.read_csv("data.csv") # Ye Yaha Pe Hui hia 
print(df.head())
# Baas Etna hi import ho gai files 

#Agar file current folder mein nahi hai:
df = pd.read_csv(r"C:\Users\Kshitij\Downloads\data.csv")   # Toh hame Uska Path dena Padhta hai

2#: Yaha pe Ek "sep" name Ka Prameter hota hai 
# sep parameter pd.read_csv() ke andar use hota hai. 
# Iska kaam batana hota hai ki columns kis character se separate hue hain.
# matlb daat ko kaise sprate karnahia wo type yaha hota hia 
# by default "," commas se Ye Chalta hai Done 

3# index_col parameter 
# kabhi aapka Essa Col ho jo apke data me kaam nahi ata hai wo Esse index me replace kar deta hai 

4# Header paramert
# header batata hai ki kaunsi row column names (headers) contain karti hai.
#1 Default: header=0  - First row is column names (default)
#2 header=None  - No header exists
#  header=n → Row number n is used as header
#3 Apne Column Names Dena
# Note : Ye read_csv() ke important parameters mein se ek hai, saath mein

5#usecols parameter 
# yaha Kabhi kabhi essa hota hai ki apko kuch col data ke usse nahi karne hote hia 
# Toh This Will Help u Ki Tum kon kon sa col use karna chahate ho wo bass wahi col leke ata hai 
# Baki Sare Col apne aap haat jate hai 
df = pd.read_csv("students.csv", usecols=['Name', 'Marks'])
# Jo Yaha List me diya hai bass wahi ayega theek 

6#squeeze parameter
#Naye Pandas versions mein squeeze remove (deprecated) ho chuka hai.

7# skiprows Parameter/ skip-n-rows  Parameter
#skiprows ka use file ki starting ki kuch rows ko ignore (skip) karne ke liye hota hai.
# Esme apa Jo parameter do ge Esse wo Skip kar denga 
df = pd.read_csv("students.csv", skiprows=2)
# Ab Ye 1, 2 Wala Rows Ko Skip kar denga studennt.csv se 
df = pd.read_csv("students.csv", skiprows=[0,5])
# Esse bhi esse Hata Sakte ho 
# Ya Fhir Tum Logic Laga Ke bhi Hata sakte ho 

# N me Bass n rows Ko hi Deta hai baki ka MAnupulate kar deta hai 
# Jaise aap Baan lo 10M ka Data Handle kar rahe ho toh usme se ye n = 100 diya apne toh esse 100 hi ayega Baki ka Dat Hata denga Done 

8# Encoding parameter 
# encoding batata hai ki file ke characters kis encoding format mein store kiye gaye hain.
# Jab Pandas file ko read karta hai aur encoding match nahi karti, tab error aata hai:
# Error : UnicodeDecodeError: 'utf-8' codec can't decode ...

# Default Encoding
# Aksar Pandas ye assume karta hai:
# df = pd.read_csv("data.csv", encoding='utf-8')
# utf-8 duniya ki sabse common encoding hai.

#Common Encodings
# | Encoding     | Use Case              |
# | ------------ | --------------------- |
# | `utf-8`      | Most modern files     |
# | `latin1`     | Older European files  |
# | `iso-8859-1` | Similar to latin1     |
# | `cp1252`     | Windows Excel exports |
# | `utf-16`     | Some special exports  |


9# Skip Badd lines .. Haan, tum jo likh rahe ho wo purane Pandas versions wale parameter ki baat hai:
# 
# Kabhi kabhi apke pass Data me Esse Rows bhi ayenge Jinsme Bich bich me ROws me data gadbad honge 
# jaise CSV mein kisi row mein expected columns se zyada ya kam values ho sakti hain. Toh ye bhi Ek Parakar ka galti hia 
# Esse pandas Read nahi kar pata hai 
# Toh Esse hatane ke liye haam Ye parmeter use karte hai 
# Skip Badd lines  esko false karna hota hai toh wo line skip ho jati hia 

# Note aaj Ke Padash me Ye 
# on_bad_lines='skip' Es name se jana jata hai 
df = pd.read_csv("data.csv", on_bad_lines='skip')

10# Ye bahut import hai taht is "Handling date "
# Actually Kya hota hai Jab bhi aap read_csv use karte ho to by default 
# jitne bhi date cols hote hai unko ass string pass kiya jata hai 
# Toh Agr wo string ban jayega date toh aap uski date ki functonalties use nahi kar paoge 
# 
# Eske Liye haam "parse_dates Use Karte hai "
df = pd.read_csv("sales.csv", parse_dates=['Date'])
# Ab Date column ka datatype: datetime64[ns]

11# converters Parameter in pd.read_csv()
# read_csv Ka Bahut hi power full feature hai 
# converters ka use tab karte hain jab tum kisi column ke data ko read karte waqt hi modify/convert karna chahte ho.
# Syntax:
pd.read_csv("file.csv", converters={'Column_Name': function})
# Example 1: Name ko Uppercase Banana
# Name,Age
# kshitij,20      ye csv data hai 
# rahul,21
# Coverter me mai dict pass karta hun theek hai na 
import pandas as pd
df = pd.read_csv("students.csv",converters={'Name': str.upper})
print(df)
# output:
#       Name  Age
# 0  KSHITIJ   20
# 1    RAHUL   21

12# na_values parameters  > bahut use hota hai.
# Iska kaam hai kuch specific values ko Missing Values (NaN) maan lena.
#Example  : CSV:
# Name,Age,Marks
# Kshitij,20,85
# Rahul,NA,90
# Priya,19,-
# Agar tum chahte ho ki "NA" aur "-" ko missing value maana jaye:
import pandas as pd
df = pd.read_csv("students.csv",na_values=['NA', '-'])
print(df)
# Output 
#       Name   Age  Marks
# 0  Kshitij  20.0   85.0
# 1    Rahul   NaN   90.0
# 2    Priya  19.0    NaN

# eske Liye Haam 
# fill na , drop na Ye sab Padha tah yad hai na 


13# "Loading a huge dataset in chunks"
# Jab dataset bahut bada ho (lakhs ya crores of rows), to poori file RAM mein load karna possible nahi hota. 
# Tab hum chunksize parameter use karte hain.

import pandas as pd
chunks = pd.read_csv("big_data.csv",chunksize=10000
)
# Yahan file 10,000 rows ke chunks mein read hogi.