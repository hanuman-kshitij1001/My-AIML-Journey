import pandas as pd
marks = {
    'maths' : 67,
    'English':85,
    'Hindi':89,
    'Physics':100,
    "Advance Backchodi":1000
}

marks_series = pd.Series(marks)
print(marks_series)
# Output
# maths                  67
# English                85
# Hindi                  89
# Physics               100
# Advance Backchodi    1000
# dtype: int64

marks = {
    'maths' : 67,
    'English':85,
    'Hindi':89,
    'Physics':100,
    "Advance Backchodi":1000
}

marks_series = pd.Series(marks, name = 'Kshitij-Tiwari')
print(marks_series)

# Dic Paass Karne Se Key Outmaticaly Index baan Jate hai 
# aur value = value 
