# YouTube Search Analyzer

A Python-based interactive application that searches YouTube videos and analyzes their views, likes, comments, engagement rate, channel performance, and title sentiment.

## 🔗 Repository

[GitHub Repository](https://github.com/ezhil1908/youtube-search-analyzer)

## 📌 Project Overview

The **YouTube Search Analyzer** is an interactive data analytics application built with Python and Streamlit.

The application allows users to search for YouTube videos using a topic or keyword and retrieve video information through the YouTube Data API.

The collected data is processed and analyzed to understand video performance based on:

- 👀 Views
- 👍 Likes
- 💬 Comments
- 📈 Engagement Rate
- 😊 Sentiment
- 📺 Channel Performance

The application presents these results through KPI cards, interactive charts, tables, filtering, sorting, and downloadable CSV reports.

This project demonstrates the practical use of **API data collection, data cleaning, exploratory data analysis, sentiment analysis, data visualization, and interactive dashboard development**.

## 🎯 Objectives

The main objectives of this project are:

- 🔎 Search and retrieve YouTube videos based on user-defined topics or keywords.
- 🧹 Clean and prepare the collected video data for analysis.
- 📊 Analyze video performance using views, likes, comments, and engagement rate.
- 📈 Identify top-performing videos based on different performance metrics.
- 📺 Analyze overall channel performance.
- 😊 Perform sentiment analysis on video titles.
- 📊 Present insights through interactive charts and visualizations.
- 🔍 Provide filtering and sorting options for easier analysis.
- 📥 Allow users to download filtered results and analytics summaries as CSV files. 

## ✨ Features

### 🔎 YouTube Video Search

- Search YouTube videos using a topic or keyword.
- Select the number of results to analyze.
- Retrieve video details using the YouTube Data API.

### 📊 Video Performance Analysis

Analyze key video performance metrics:

- Views
- Likes
- Comments
- Engagement Rate
- Like Rate
- Comment Rate
- Video Duration

### 🏆 Top Performing Videos

Identify videos with:

- Highest Views
- Highest Likes
- Highest Comments
- Highest Engagement Rate

### 📺 Channel Performance Analysis

Analyze channel-level performance using:

- Total Videos
- Total Views
- Total Likes
- Total Comments
- Average Engagement Rate

### 😊 Sentiment Analysis

Analyze video titles and classify them into:

- Positive
- Neutral
- Negative

### 📈 Interactive Visualizations

The dashboard provides visualizations for:

- Views by Video
- Likes by Video
- Top 5 Videos by Engagement Rate
- Views vs Engagement Rate
- Total Views by Channel
- Video Sentiment Distribution

### 🔍 Filtering and Sorting

Users can filter and sort the search results based on different performance metrics.

Available sorting options include:

- Views
- Likes
- Comments
- Engagement Rate

### 📥 Download Results

Users can download:

- Filtered video results as CSV
- Analytics summary as CSV

### 🎥 Video Viewing

Users can select a video from the results and view it directly through the application.

## 🔄 Project Workflow

The project follows the workflow below:

```text
User Search Topic
        ↓
YouTube Data API
        ↓
Video Data Collection
        ↓
Data Cleaning & Preparation
        ↓
Feature Engineering
        ↓
Engagement & Performance Analysis
        ↓
Sentiment Analysis
        ↓
Interactive Visualizations
        ↓
Filtering & Sorting
        ↓
Insights & CSV Export 
```


## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language used for data collection, processing, analysis, and application development |
| 🎈 Streamlit | Used to build the interactive web application and dashboard |
| 🐼 Pandas | Used for data cleaning, transformation, aggregation, and analysis |
| 📊 Plotly | Used to create interactive data visualizations |
| ▶️ YouTube Data API | Used to search YouTube videos and retrieve video statistics |
| 😊 TextBlob | Used for sentiment analysis of video titles |
| 🔐 python-dotenv | Used to securely load the YouTube API key from the `.env` file |
| 🔗 Google API Client | Used to connect and communicate with the YouTube Data API |
| 📁 CSV | Used for storing and exporting video and analytics data |
| 🌿 Git & GitHub | Used for version control and project management |

## 📊 Analytics Performed

The project calculates and analyzes several key YouTube performance metrics.

### 👀 Views Analysis

Analyzes the total and individual video views to identify the most viewed videos and compare video reach.

### 👍 Likes Analysis

Analyzes total and individual video likes to identify videos that receive higher audience appreciation.

### 💬 Comments Analysis

Analyzes comments to understand audience interaction and identify videos generating higher discussion.

### 📈 Engagement Rate

The engagement rate is calculated using:

**Engagement Rate = ((Likes + Comments) / Views) × 100**

This metric helps compare audience interaction relative to the number of video views.

### 👍 Like Rate

The like rate is calculated using:

**Like Rate = (Likes / Views) × 100**

This helps measure the proportion of viewers who expressed appreciation through likes.

### 💬 Comment Rate

The comment rate is calculated using:

**Comment Rate = (Comments / Views) × 100**

This helps measure the level of audience interaction through comments.

### 🏆 Top Video Analysis

The application identifies top-performing videos based on:

- Views
- Likes
- Comments
- Engagement Rate

### 📺 Channel Performance

The application aggregates video-level data by channel to compare:

- Total Videos
- Total Views
- Total Likes
- Total Comments
- Average Engagement Rate

### 📊 Comparative Analysis

The dashboard allows users to compare video performance through interactive charts, tables, filtering, and sorting.

## 😊 Sentiment Analysis

The project performs sentiment analysis on YouTube video titles using **TextBlob**.

Each video title is analyzed using its polarity score and classified into one of three categories:

- 😊 **Positive**
- 😐 **Neutral**
- 😞 **Negative**

### 🔍 Sentiment Process

```text
YouTube Video Title
        ↓
Text Preprocessing
        ↓
TextBlob Polarity Analysis
        ↓
Polarity Score
        ↓
Positive / Neutral / Negative
```

## 📈 Dashboard & Visualizations

The Streamlit dashboard presents the analyzed YouTube data through interactive charts, KPI metrics, and tables.

### 📊 Key Performance Indicators

The dashboard displays important summary metrics such as:

- 🎬 Total Videos
- 👀 Average Views
- 👍 Average Likes
- 📈 Average Engagement Rate

### 🏆 Top 5 Videos by Engagement

A horizontal bar chart displays the top 5 videos based on engagement rate, making it easy to identify videos with stronger audience interaction.

### 👀 Views by Video

A visual comparison of video views helps identify which videos achieved greater reach.

### 👍 Likes by Video

A horizontal bar chart compares the number of likes received by different videos.

### 📈 Views vs Engagement Rate

This visualization compares video reach with engagement rate to help identify videos that achieve both high visibility and strong audience interaction.

### 📺 Channel Performance Analysis

Channel-level analysis summarizes:

- Total Videos
- Total Views
- Total Likes
- Total Comments
- Average Engagement Rate

A channel-level views chart is also provided for comparison.

### 😊 Sentiment Distribution

A bar chart displays the distribution of:

- Positive videos
- Neutral videos
- Negative videos

### 📋 Interactive Data Table

The dashboard provides the analyzed video data in a table, allowing users to inspect individual video metrics.

### 🔍 Filtering

Users can filter the displayed results using available filters such as:

- Sentiment
- Minimum Views

### 🔽 Sorting

Users can sort the video results by:

- Views
- Likes
- Comments
- Engagement Rate


## 📂 Project Structure

```text
youtube-search-analyzer/
│
├── data/
│   ├── videos.csv
│   └── cleaned_videos.csv
│
├── analysis.py
├── api.py
├── app.py
├── sentiment.py
├── visualization.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

Clone the Repository:git clone https://github.com/ezhil1908/youtube-search-analyzer.git
Navigate to the project directory:cd youtube-search-analyzer
Create a Python virtual environment:python -m venv venv
Activate the Virtual Environment: venv\Scripts\activate
Install the required Python packages:pip install -r requirements.txt
Create a .env file in the project root directory:
youtube-search-analyzer/
│
├── .env
├── app.py
├── api.py
└── ...
Add your API key to the .env file:YOUTUBE_API_KEY=your_api_key_here

## ▶️ How to Run the Application

After completing the installation and API configuration, run the Streamlit application using:
streamlit run app.py

## 📥 Export Results

The application allows users to download analyzed data for further use.

Available downloads include:

- 📄 **Filtered Results (CSV)** – Downloads the videos matching the selected filters.
- 📊 **Analytics Summary (CSV)** – Downloads the calculated analytical metrics and insights.

These exported files can be used for further analysis or reporting in tools such as Excel, Power BI, or other data analytics platforms.

## 🚀 Future Improvements

Potential improvements for the project include:

- 📈 Add historical YouTube performance tracking.
- 📊 Add time-series analysis of video performance.
- 🔎 Add keyword and topic-level analysis.
- 📺 Add detailed channel comparison.
- 🖼️ Add thumbnail analysis.
- 🧠 Improve sentiment analysis using advanced NLP models.
- 📊 Add more advanced interactive dashboard features.
- ☁️ Deploy the application online using Streamlit Cloud.


👨‍💻 Author
Ezhilvendhan P
MBA – Data Analytics
Linkedin: https://www.linkedin.com/in/ezhilvendhan1908/
GitHub: https://github.com/ezhil1908
