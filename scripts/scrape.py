from google_play_scraper import reviews, Sort
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, app_id in apps.items():
    result, _ = reviews(
        app_id,
        lang="en",
        country="et",
        sort=Sort.NEWEST,
        count=500
    )

    for r in result:
        if r["content"] and r["score"]:
            all_reviews.append({
                "review": r["content"],
                "rating": r["score"],
                "date": r["at"].strftime("%Y-%m-%d"),
                "bank": bank,
                "source": "Google Play"
            })

df = pd.DataFrame(all_reviews)

# CLEANING
df = df.drop_duplicates()
df = df.dropna(subset=["review", "rating"])

# SAVE
output_path = "data/raw/reviews.csv"
df.to_csv(output_path, index=False)

# CHECKS
print("DONE:", len(df))
print(df["bank"].value_counts())