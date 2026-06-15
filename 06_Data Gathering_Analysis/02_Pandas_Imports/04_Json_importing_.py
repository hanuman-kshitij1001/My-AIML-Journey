# JSON (JavaScript Object Notation)
# Ab hum dekhenge ki JSON files ke saath kaise kaam karte hain.

# JSON ek lightweight data format hai jiska use data ko store aur transfer
# karne ke liye kiya jata hai.
# Aaj ke time mein lagbhag saari APIs data JSON format mein hi return karti hain.
# JSON data key-value pair ke form mein store hota hai.
# Example:
# {
#     "name":"Kshitij",
#     "age":20,
#     "branch":"CSE"
# }

# Yahan:
# name, age, branch -> Keys
# Kshitij, 20, CSE -> Values

# JSON ka use:
# 1. APIs se data fetch karne mein
# 2. Web applications mein
# 3. Data exchange karne mein
# 4. Configuration files mein

# Pandas mein JSON file ko read karne ke liye:
# pd.read_json()

# Example:
# df = pd.read_json('students.json')

# Agar JSON internet par kisi URL par hai:
# df = pd.read_json(url)
# Real-world mein JSON data aksar nested hota hai.
# Nested JSON ko flat table mein convert karne ke liye:
# pd.json_normalize()

# Important:
# CSV rows aur columns mein data store karta hai.
# JSON key-value pairs aur nested structures ko support karta hai.

# Data Analysis mein JSON bahut important hai kyunki APIs se aane wala
# adhiktar data JSON format mein hota hai.





# 1. JSON Data Import
#    JSON ka full form hai JavaScript Object Notation.
# Example JSON:
[
    {
        "Name": "Kshitij",
        "Age": 20,
        "Marks": 85
    },
    {
        "Name": "Rahul",
        "Age": 21,
        "Marks": 90
    }
]

#Read karne ke liye: Tarika Ya Syntax 
import pandas as pd
df = pd.read_json("students.json")
print(df)


#       Name  Age  Marks
# 0  Kshitij   20     85
# 1    Rahul   21     90

