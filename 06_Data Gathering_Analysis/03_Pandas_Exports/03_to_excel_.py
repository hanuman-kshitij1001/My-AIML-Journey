# For excel use this syntax
# "   to_excel   "

import pandas as pd

data = {
    "Name": ["Kshitij", "Rahul", "Aman"],
    "Age": [20, 21, 22]
}

df = pd.DataFrame(data)

df.to_excel("output.xlsx")
# Yah Pe df.to_excel("Ess name Se ") ek Puri ki puri file bana denga done 