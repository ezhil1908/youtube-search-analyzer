import os
import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load API key
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")


def search_youtube(search_query, num_results=5):

    youtube = build(
        "youtube",
        "v3",
        developerKey=API_KEY
    )

    # Search videos
    search_request = youtube.search().list(
        part="snippet",
        q=search_query,
        type="video",
        maxResults=num_results
    )

    search_response = search_request.execute()
    print("SEARCH RESULTS:", len(search_response["items"]))
    video_ids = [
        item["id"]["videoId"]
        for item in search_response["items"]
    ]
    print("VIDEO IDS:", len(video_ids))
    if not video_ids:
        return pd.DataFrame()

    # Get video statistics and duration
    video_request = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        id=",".join(video_ids)
    )

    video_response = video_request.execute()
    print("VIDEO DETAILS:", len(video_response["items"]))
    videos = []

    for video in video_response["items"]:

        statistics = video.get("statistics", {})
        snippet = video.get("snippet", {})
        content = video.get("contentDetails", {})

        videos.append({
            "video_id": video["id"],
            "title": snippet.get("title", ""),
            "channel": snippet.get("channelTitle", ""),
            "published_at": snippet.get("publishedAt", ""),
            "views": int(statistics.get("viewCount", 0)),
            "likes": int(statistics.get("likeCount", 0)),
            "comments": int(statistics.get("commentCount", 0)),
            "duration": content.get("duration", ""),
            "video_url": f"https://www.youtube.com/watch?v={video['id']}"
        })

    return pd.DataFrame(videos)