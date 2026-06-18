1#. Exporting To CSV
# Sabse common export format.
# Basic Syntax: df.to_csv("output.csv")

# Ex:
import pandas as pd
df = pd.DataFrame({
    'Name':['Kshitij','Rahul'],
    'Marks':[85,90]
})
df.to_csv("students.csv")
# Ye ek nayi file bana dega:  students.csv  se 
# Bass Yahi Tarika hai Csv me Banane ke Theek hai na 
