import pandas as pd
from sqlalchemy import create_engine

print("SCRIPT STARTED")

# ---------------- DATABASE CONNECTION ----------------
username = "postgres"
password = "1234567"
host = "localhost"
port = "5432"
database = "bank_reviews"

engine = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/{database}"
)

print("STARTING DATABASE INSERT")

# ---------------- LOAD CSV ----------------
df = pd.read_csv("data/raw/reviews_sentiment_themes.csv")

print("CSV Loaded:", len(df))

# ---------------- INSERT BANKS ----------------
banks_df = pd.DataFrame({
    "bank_name": ["CBE", "BOA", "Dashen"],
    "app_name": [
        "Commercial Bank of Ethiopia",
        "Bank of Abyssinia",
        "Dashen Bank"
    ]
})

banks_df.to_sql(
    "banks",
    engine,
    if_exists="append",
    index=False
)

# ---------------- MAP BANK IDS ----------------
bank_mapping = {
    "CBE": 1,
    "BOA": 2,
    "Dashen": 3
}

df["bank_id"] = df["bank"].map(bank_mapping)

# ---------------- SELECT REVIEW COLUMNS ----------------
reviews_df = df[
    [
        "bank_id",
        "review",
        "rating",
        "date",
        "sentiment",
        "sentiment_score",
        "theme",
        "source"
    ]
]

# ---------------- RENAME COLUMNS ----------------
reviews_df.columns = [
    "bank_id",
    "review_text",
    "rating",
    "review_date",
    "sentiment_label",
    "sentiment_score",
    "identified_theme",
    "source"
]

# ---------------- INSERT REVIEWS ----------------
reviews_df.to_sql(
    "reviews",
    engine,
    if_exists="append",
    index=False
)

print("Inserted Reviews:", len(reviews_df))

print("TASK 3 COMPLETED")