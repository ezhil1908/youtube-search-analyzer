import pandas as pd
import re

# -----------------------------
# 1. Load raw YouTube data
# -----------------------------

df = pd.read_csv("data/videos.csv")

print("Raw Data:")
print(df)

print("\nData Types:")
print(df.dtypes)


# -----------------------------
# 2. Convert numeric columns
# -----------------------------

df["views"] = pd.to_numeric(df["views"], errors="coerce")
df["likes"] = pd.to_numeric(df["likes"], errors="coerce")
df["comments"] = pd.to_numeric(df["comments"], errors="coerce")


# -----------------------------
# 3. Convert published date
# -----------------------------

df["published_at"] = pd.to_datetime(
    df["published_at"],
    errors="coerce"
)


# -----------------------------
# 4. Convert YouTube duration
# -----------------------------

def duration_to_seconds(duration):
    match = re.match(
        r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?",
        duration
    )

    if not match:
        return 0

    hours = int(match.group(1) or 0)
    minutes = int(match.group(2) or 0)
    seconds = int(match.group(3) or 0)

    return hours * 3600 + minutes * 60 + seconds


df["duration_seconds"] = df["duration"].apply(duration_to_seconds)


# -----------------------------
# 5. Create duration in minutes
# -----------------------------

df["duration_minutes"] = (
    df["duration_seconds"] / 60
).round(2)


# -----------------------------
# 6. Calculate engagement rate
# -----------------------------

df["engagement_rate"] = (
    (df["likes"] + df["comments"])
    / df["views"]
    * 100
).round(2)


# -----------------------------
# 7. Like rate
# -----------------------------

df["like_rate"] = (
    df["likes"]
    / df["views"]
    * 100
).round(2)


# -----------------------------
# 8. Comment rate
# -----------------------------

df["comment_rate"] = (
    df["comments"]
    / df["views"]
    * 100
).round(2)


# -----------------------------
# 9. Add search ranking
# -----------------------------

df["search_rank"] = range(1, len(df) + 1)


# -----------------------------
# 10. Display cleaned data
# -----------------------------

print("\nCleaned Data:")
print(df)


# -----------------------------
# 11. Save cleaned dataset
# -----------------------------

df.to_csv(
    "data/cleaned_videos.csv",
    index=False
)

print("\nCleaned data saved successfully!")

# -----------------------------
# EDA - Basic Statistics
# -----------------------------

print("\nBasic Statistics:")
print(df[[
    "views",
    "likes",
    "comments",
    "duration_minutes",
    "engagement_rate"
]].describe())
# -----------------------------
# Top videos by views
# -----------------------------

top_views = df.sort_values(
    by="views",
    ascending=False
)

print("\nTop Videos by Views:")
print(
    top_views[
        ["title", "channel", "views", "likes", "comments"]
    ].to_string(index=False)
)
# -----------------------------
# Top videos by engagement
# -----------------------------

top_engagement = df.sort_values(
    by="engagement_rate",
    ascending=False
)

print("\nTop Videos by Engagement Rate:")
print(
    top_engagement[
        ["title", "channel", "views", "engagement_rate"]
    ].to_string(index=False)
)
# -----------------------------
# Top videos by comments
# -----------------------------

top_comments = df.sort_values(
    by="comments",
    ascending=False
)

print("\nTop Videos by Comments:")
print(
    top_comments[
        ["title", "channel", "comments", "views"]
    ].to_string(index=False)
)
