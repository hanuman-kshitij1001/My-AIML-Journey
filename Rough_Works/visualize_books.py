import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
df = pd.read_csv("books_cleaned.csv")

sns.set_style("whitegrid")

# ---- Chart 1: Average Price by Rating ----
plt.figure(figsize=(8, 5))
avg_price = df.groupby("Rating")["Price (GBP)"].mean().reset_index()
sns.barplot(data=avg_price, x="Rating", y="Price (GBP)", palette="Blues_d")
plt.title("Average Book Price by Rating", fontsize=14, fontweight="bold")
plt.xlabel("Rating (Stars)")
plt.ylabel("Average Price (GBP)")
plt.tight_layout()
plt.savefig("chart_price_by_rating.png", dpi=150)
plt.show()

# ---- Chart 2: Price Distribution ----
plt.figure(figsize=(8, 5))
sns.histplot(df["Price (GBP)"], bins=15, kde=True, color="steelblue")
plt.title("Price Distribution of Books", fontsize=14, fontweight="bold")
plt.xlabel("Price (GBP)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("chart_price_distribution.png", dpi=150)
plt.show()

# ---- Chart 3: Rating Count ----
plt.figure(figsize=(8, 5))
rating_counts = df["Rating"].value_counts().sort_index()
sns.barplot(x=rating_counts.index, y=rating_counts.values, palette="Greens_d")
plt.title("Number of Books per Rating", fontsize=14, fontweight="bold")
plt.xlabel("Rating (Stars)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("chart_rating_count.png", dpi=150)
plt.show()

print("All 3 charts saved successfully!")