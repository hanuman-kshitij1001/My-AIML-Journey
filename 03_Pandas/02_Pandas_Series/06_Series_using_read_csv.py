# Abhi Tak Series hamne Python list e banay ya Dic se banay lekin ab haam Real Data set se resies banane wale hai 
# Ek Function Hai Read csv files 

# data Set link : https://drive.google.com/drive/folders/1IfYgDQzE8B_VOAik6Qha06Ok-NXLb98q

# Suno Hame Kya karna hAi En Files ke Through Series Object banane hai 
# Ab In Data Set ko import karenge inide this folder Aur unhe Use karke 

# Sabse Pahle Hum Subs.cvs kya hai Ye kya hai # Ye sir ka Data hai Esme ye hia ki sir ke channe ne kitne subscripser gain kiya 
# Chalo Esse Series me convert karte hia 
import pandas as pd
import pandas as pd

df = pd.read_csv('03_Pandas/02_Pandas_Series/09_DataSet_subs.csv')
print(df.head()) 
print(type(df))  # <class 'pandas.core.frame.DataFrame'>
# Matlb Ess Traha Likhne Se ye data frame bana na ki series toh kya kare 


# Apko Bass Ek Chota sa change karna hai that is Ek Pracmeter hai 
df = pd.read_csv('03_Pandas/02_Pandas_Series/09_DataSet_subs.csv')
s = df.squeeze()   # ye Data Frame Nahi Banne De raha Hai Queeze bana de raha hai 
print(type(s))
print(s.head())
# Ye sahi se nahi bane hai 
