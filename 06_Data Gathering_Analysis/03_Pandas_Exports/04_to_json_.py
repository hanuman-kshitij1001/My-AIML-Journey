# JSON Export
# Ye bahut important hai, especially AIML, APIs, Web Development, Data Engineering sab jagah use hota hai.

#What is JSON?  = JSON = JavaScript Object Notation
#Ye data store aur exchange karne ka lightweight format hai

#Example : 
{
    "Name": "Kshitij",
    "Age": 20
}
#Human-readable bhi hai aur machines ke liye bhi easy hai.

# Why JSON?

# CSV aur Excel humans ke liye acche hain, lekin applications ke beech data transfer ke liye JSON zyada popular hai.
# Example:
# APIs
# Web Applications
# Mobile Apps
# ML Models
# Configuration Files

# Jab tum kisi API se data loge, 90% chance hai ki JSON format me milega.

#Basic Syntax  : df.to_json("students.json")

# Example :
import pandas as pd

data = {
    "Name": ["Kshitij", "Rahul", "Aman"],
    "Age": [20, 21, 22]
}

df = pd.DataFrame(data)

df.to_json("students.json")


# Output: JSON
{
    "Name":{
        "0":"Kshitij",
        "1":"Rahul",
        "2":"Aman"
    },
    "Age":{
        "0":20,
        "1":21,
        "2":22
    }
}

# Different JSON Formats (Orient)
# 1. orient='records' ⭐ Most Important  
#    Ye decide karta hai JSON kis structure me banega.

# Ex : 
df.to_json(
    "students.json",
    orient="records"
)
# Output :  Ye API format hai aur sabse zyada use hota hai.
[
    {
        "Name":"Kshitij",
        "Age":20
    },
    {
        "Name":"Rahul",
        "Age":21
    },
    {
        "Name":"Aman",
        "Age":22
    }
]

# 2. orient='index'
df.to_json(orient='index')

# Output:   
{
    "0":{"Name":"Kshitij","Age":20},
    "1":{"Name":"Rahul","Age":21},
    "2":{"Name":"Aman","Age":22}
}

#3. orient='columns' (Default)
df.to_json(orient='columns')
# Output::

{
    "Name":{
        "0":"Kshitij",
        "1":"Rahul"
    },
    "Age":{
        "0":20,
        "1":21
    }
}

# 4. orient='values'
df.to_json(orient='values')

# OutPut: Sirf values aayengi, column names nahi.

[
    ["Kshitij",20],
    ["Rahul",21]
]

# 5. orient='split'