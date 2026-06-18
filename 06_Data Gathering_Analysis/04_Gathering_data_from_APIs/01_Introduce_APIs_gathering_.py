# Note :Pandas me Data Gathering from APIs bahut important topic hai, especially Data Analysis aur Machine Learning me. 


# API Kya Hoti Hai?
# API = Application Programming Interface

# Simple language me:
# API ek waiter ki tarah hoti hai jo tumhare application aur server/database ke beech communication karwati hai.

# Example:
# Your Python Code
#        ↓
#       API
#        ↓
#     Server
#        ↓
#    Required Data

# Real Life Example

# Maan lo tum weather data chahte ho.
# Tum directly weather company ke database me nahi ja sakte.
# Tum API ko request bhejte ho:   "Mumbai ka weather batao"

# API response bhejti hai: JSON
{
  "city":"Mumbai",
  "temp":30,
  "humidity":75
}


# Python Me API Se Data Kaise Lete Hain?
# Sabse common library:
import requests
# Agar install na ho:  # pip install requests

# Step 1: API Call
# Example API:

import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
print(response)

# Output:
# <Response [200]>

# Check:
print(response.status_code)

# Step 2: JSON Data Extract Karna
# Most APIs JSON return karti hain.
data = response.json()
print(data)
# Output:
[
 {
   "id":1,
   "name":"Leanne Graham"
 },
 {
   "id":2,
   "name":"Ervin Howell"
 }
]

# Step 3: Pandas DataFrame Banana
import pandas as pd
df = pd.DataFrame(data)
print(df.head())
# Output:
#    id           name
# 0   1  Leanne Graham
# 1   2   Ervin Howell
# ...


# One-Liner
# API → JSON → DataFrame

import requests
import pandas as pd
url = "https://jsonplaceholder.typicode.com/users"
data = requests.get(url).json()
df = pd.DataFrame(data)
print(df.head())

# Nested JSON Problem
# Kai baar JSON ke andar aur JSON hota hai.

{
   "id":1,
   "name":"Kshitij",
   "address":{
      "city":"Mumbai",
      "pin":400001
   }
}
# Normal DataFrame: 
# df = pd.DataFrame(data)
# Output:  id  name  address
# Address ek dictionary ban jayega.



# Solution: json_normalize()
pd.json_normalize(data)
# Output:   id name city pin
# Nested data flatten ho jayega.






