import pandas as pd

df = pd.read_csv("data/raw/reviews.csv")

print("\nREVIEWS PER BANK:")
print(df["bank"].value_counts())

print("\nAVERAGE RATING PER BANK:")
print(df.groupby("bank")["rating"].mean())

print("\nOVERALL SUMMARY:")
print(df["rating"].describe())