import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer

# download required model once
nltk.download("vader_lexicon")


# ---------------- SENTIMENT FUNCTION ----------------
def get_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(str(text))["compound"]

    if score >= 0.05:
        return "positive", score
    elif score <= -0.05:
        return "negative", score
    else:
        return "neutral", score


# ---------------- THEME FUNCTION ----------------
def extract_theme(text):
    text = str(text).lower()

    if "login" in text or "sign in" in text:
        return "Login Issues"
    elif "slow" in text or "transfer" in text:
        return "Transaction Performance"
    elif "otp" in text or "code" in text:
        return "OTP / Authentication"
    elif "crash" in text or "error" in text:
        return "App Stability"
    elif "ui" in text or "design" in text:
        return "UI / UX"
    else:
        return "Other"


# ---------------- PIPELINE ----------------
def run_pipeline(df):
    df["sentiment"], df["sentiment_score"] = zip(
        *df["review"].apply(get_sentiment)
    )

    df["theme"] = df["review"].apply(extract_theme)

    return df


# ---------------- MAIN EXECUTION ----------------
if __name__ == "__main__":
    df = pd.read_csv("data/raw/reviews.csv")

    df = run_pipeline(df)

    df.to_csv(
        "data/raw/reviews_sentiment_themes.csv",
        index=False
    )

    print("Sentiment distribution:")
    print(df["sentiment"].value_counts())

    print("\nTheme distribution:")
    print(df["theme"].value_counts())

    print("\nDONE TASK 2")