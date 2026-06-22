# Set Up 

import re

import pandas as pd
import numpy as np
adverse_reactions = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/01_adverse_reactions.csv")
patients = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/02_patients.csv")
treatments = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/03_treatments.csv")
treatments_cut = pd.read_csv("07_Data_Assessing_nd_Cleaning/Data_set/04_treatments_cut.csv")

print(adverse_reactions)
print(patients)
print(treatments)
print(treatments_cut)



#1- # code
patients_df = patients.fillna('No data',inplace=True)   # Ye haam Missing Data Fill Kar rahe 
print(patients_df)   # Ye haam print kar rahe hain taake ham dekh saken ke Missing Data Fill Hua ya nahi


# test
patients_df.info()

# 2- # code
treatments.head()

#
# code : Ye kya Kar raha hun mai: actually mai Yaha Pe HbA1c Change Nikal raha hun, HbA1c Change Nikalne ke liye Mai Start Value me se End Value Ko Minus Kar raha hun, Taake Mai Ye Deh Sakan Ke HbA1c Me Kya Change Aaya Hai, Agar HbA1c Change Positive Aaya To Matlab HbA1c Me Kami Aayi Hai, Aur Agar HbA1c Change Negative Aaya To Matlab HbA1c Me Badhotri Aayi Hai, Aur Agar HbA1c Change Zero Aaya To Matlab HbA1c Me Koi Change Nahi Aaya Hai.
treatments['hba1c_change'] = treatments['hba1c_start'] - treatments['hba1c_end']
treatments_cut['hba1c_change'] = treatments_cut['hba1c_start'] - treatments_cut['hba1c_end']
# ab apke data me koi bhi missing value nahi hai, to aapko koi bhi missing value fill karne ki zarurat nahi hai, aur aap apne analysis me aage badh sakte hain.

import re
def find_contact_details(text: str) -> tuple:
    # it the value is NaN, then return it
    if pd.isna(text):
        return np.nan
    
    # create the phone number pattern
    phone_number_pattern = re.compile(r"(\+[\d]{1,3}\s)?(\(?[\d]{3}\)?\s?-?[\d]{3}\s?-?[\d]{4})")
    # find the phone number from the value/text, as a result we will get a list
    phone_number  = re.findall(phone_number_pattern, text)

    # if length is 0, then the regex can't find any ph number, then define with NaN
    if len(phone_number) <= 0:
        phone_number = np.nan
    # if the country code is attached with the ph number, for that case, the first
    # element will be the country code and the 2nd element will be the actual ph
    # number. So, get that ph number
    elif len(phone_number) >= 2:
        phone_number = phone_number[1]
    # else, we will get the ph number. Grab it.
    else:
        phone_number = phone_number[0]

    # if we found the ph number (with/without country code), then remove that part from the actual value.
    # after removing the ph number, the remaining string might be the email address.
    possible_email_add = re.sub(phone_number_pattern, "", text).strip()

    # then return the ph number and the email address
    return phone_number, possible_email_add
