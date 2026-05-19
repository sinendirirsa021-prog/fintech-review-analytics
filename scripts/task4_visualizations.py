import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/raw/reviews_sentiment_themes.csv")

# ---------------- SENTIMENT DISTRIBUTION ----------------
plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="sentiment",
    hue="bank"
)

plt.title("Sentiment Distribution by Bank")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("sentiment_distribution.png")

plt.show()

# ---------------- RATING DISTRIBUTION ----------------
plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x="bank",
    y="rating"
)

plt.title("Rating Distribution per Bank")
plt.xlabel("Bank")
plt.ylabel("Rating")

plt.tight_layout()

plt.savefig("rating_distribution.png")

plt.show()

# ---------------- THEME FREQUENCY ----------------
plt.figure(figsize=(10,5))

theme_counts = df["theme"].value_counts()

sns.barplot(
    x=theme_counts.values,
    y=theme_counts.index
)

plt.title("Theme Frequency Analysis")
plt.xlabel("Count")
plt.ylabel("Theme")

plt.tight_layout()

plt.savefig("theme_frequency.png")

plt.show()

print("TASK 4 VISUALIZATIONS COMPLETED")