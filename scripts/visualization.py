import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/reviews.csv")

counts = df["bank"].value_counts()

counts.plot(kind="bar")

plt.title("Number of Reviews per Bank")
plt.xlabel("Bank")
plt.ylabel("Review Count")

plt.tight_layout()

plt.savefig("bank_distribution.png")
plt.show()