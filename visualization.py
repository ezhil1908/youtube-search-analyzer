import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load cleaned data
# -----------------------------

df = pd.read_csv("data/cleaned_videos.csv")


# -----------------------------
# Top 5 videos by views
# -----------------------------

top_videos = df.sort_values(
    by="views",
    ascending=False
).head(5)


# -----------------------------
# Create bar chart
# -----------------------------

plt.figure(figsize=(12, 6))

plt.bar(
    top_videos["title"],
    top_videos["views"]
)

plt.title("Top YouTube Videos by Views")
plt.xlabel("Video")
plt.ylabel("Views")

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()
plt.show()