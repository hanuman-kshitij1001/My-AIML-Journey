# Web Scraping ka matlab hota hai:
#  Kabhi kabhi esa hota hai 
# Direct APis nahi hoti hai 
# Direct data nahi mil raha hota hai 
# toh Waha Haam Data lane Ke liye web scrapping use karte hai Kyu Yahi Last option hota hai 
# 

import pandas as pd
import requests
from bs4 import BeautifulSoup
# Ye Sab Hari Scapping Library hai 

response = requests.get('https://www.ambitionbox.com/list-of-companies?page=1')
print(response)   # <Response [403]>   Eska Matlb Server ne Tumare Baad Request ko Reject kar diya hai 


response = requests.get('https://www.ambitionbox.com/list-of-companies?page=1').text
# agr tumm esse likhte ho toh tumhe yaha content milega jo batayega kya problem hai 
print(response)

# Actually yaaha Pe kya ho raha hai na ki Ye Jo website hai na 
# Enlongo ne there is a thing web devlopment me ek comcept hota hai called 
# rubots.txt ka  waha pe tum ek text file me un files ka name likh dete ho jisko tum chahte ho ki web scrappers ya fhir google jaisa search engine call na paye toh uss robote .text me jin files ka name dal donge unko tum esse directly excess nahi kar paoge 
# Eske Haam Solution Bata hun ki 
# Ki TUm pane Ap ko Disguide me essa show Karo jaise ye request browser ke throught a raha hai 
# matlb ek Essa kind of extra header bhejoge Jisse us Web ko lagega ki koi bot nahi a raha hai huaman hi a raha hai 

# to eska Code hota hai 

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'} 
web_page = requests.get('https://www.ambitionbox.com/list-of-companies?page=1',headers=headers).text

# jab Tum Esko Run Karoge Toh Tumhare pass pura ka pura html ka Code jayega 
# Accha ek Baat Ye Uss Web Page direct jake page 1 pe inpect karoge same wahi code milega jo tum abhi yaha python me fetch kiye ho 
# Usse mai Ek Variable me Stroe kar deta hun Age kaam ayega varibale name

# Use parse karne usse necesary information nikalna bacha hia bass wahi hamra main goal hai 

# aur wahi pe hamko   "BeautifulSoup" library ka kaam padega 

soup = BeautifulSoup(web_page, 'lxml')  # esse run karoge toh tumhara soup wala variiable creat ho jayega theek hai na 

print(soup.prettify())  # ye kya karega Tumhare html ke pure page ko fomate kar denga theek hai na 

print(soup.findAll('h1'))

h1_count = len(soup.find_all('h1'))
print(h1_count)


# soup.find()       # first tag
# soup.find_all()   # all tags
# len(...)          # count
# tag.text          # text extract
# tag['href']       # attribute extract



# TO FIND OUT THE RATINGS
len(soup.find_all('p',class_='rating'))
     


# TO FIND OUT THE NUMBER OF REVIEWS
len(soup.find_all('a' , class_='review-count'))


# CONSIDERING THE WHOLE CONTAINER
company=soup.find_all('div',class_='company-content-wrapper')
     
      
# 
#creating dataframe for all the pages
