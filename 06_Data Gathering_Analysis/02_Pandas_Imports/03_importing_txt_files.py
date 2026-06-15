# Text File Import (.txt) padhate hain.
# Note : Aap ko Jab bhi text ko import ya call karna hia ap hamesh read_csv ko hi call karoge theek hai na 
# Text File Kya Hoti Hai?
# Simple text file, jaise:

# students.txt

# Name,Age,Marks
# Kshitij,20,85
# Rahul,21,90
# Priya,19,88

# Agar data comma-separated hai, to usse CSV ki tarah hi read kar sakte ho:

import pandas as pd
df = pd.read_csv("students.txt")
print(df)

#Tab-Separated Text File
# students.txt
# Name    Age    Marks
# Kshitij 20     85
# Rahul   21     90
# Priya   19     88
# Yahan columns Tab (\t) se separate hain.

# Pipe-Separated Text File
# Whitespace-Separated Data