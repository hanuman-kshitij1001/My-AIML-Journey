

"""
Portfolio Project: Web Scraping + Data Cleaning + Visualization
Source: books.toscrape.com (a public practice site, scraping allowed)
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

books = []

# Scrape first 5 pages (~100 books)
for page in range(1, 6):
    url = BASE_URL.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    book_items = soup.find_all("article", class_="product_pod")

    for item in book_items:
        title = item.h3.a["title"]
        price_text = item.find("p", class_="price_color").text
        price = float(re.sub(r"[^\d.]", "", price_text))

        rating_class = item.find("p", class_="star-rating")["class"][1]
        rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        rating = rating_map.get(rating_class, 0)

        availability = item.find("p", class_="instock availability").text.strip()
        in_stock = "In stock" in availability

        books.append({
            "Title": title,
            "Price (GBP)": price,
            "Rating": rating,
            "In Stock": in_stock
        })

    print(f"Page {page} done. Total books so far: {len(books)}")

print(f"\nScraped {len(books)} books successfully.")

# ---- Convert to DataFrame ----
df = pd.DataFrame(books)

print("\nRaw scraped data sample:")
print(df.head())

# ---- Data Cleaning ----
df.drop_duplicates(subset="Title", inplace=True)
df["Title"] = df["Title"].str.strip()
df.dropna(inplace=True)

print(f"\nAfter cleaning: {len(df)} unique books remain.")

# Save cleaned data
df.to_csv("books_cleaned.csv", index=False)
print("\nSaved cleaned data to books_cleaned.csv")
print(df.describe())