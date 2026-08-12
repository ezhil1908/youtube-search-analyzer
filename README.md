# 🎬 YouTube Search Analyzer

A Python-based data analytics web application that searches YouTube videos and analyzes their performance using views, likes, comments, engagement rate, sentiment analysis, filtering, sorting, and interactive visualizations.

## 📌 Project Overview


The **YouTube Search Analyzer** allows users to enter a YouTube search topic and retrieve relevant videos.

The application analyzes the retrieved videos and provides insights into:

- 👀 Views
- 👍 Likes
- 💬 Comments
- 📈 Engagement Rate
- 😊 Sentiment
- 🏆 Top Performing Videos
- 🔍 Video Filtering
- ↕️ Video Sorting
- 📊 Interactive Visualizations
- 📥 CSV Analytics Downloads

The project was developed using Python and Streamlit with a focus on practical data analytics and visualization.

## 🚀 Features
### 🔎 YouTube Search


Search for videos using any topic or keyword.

Example:

```text
Data Analytics

The application retrieves available YouTube search results and displays important video information.

📊 Performance Overview

The dashboard provides overall performance metrics:

Total Videos
Total Views
Total Likes
Average Engagement Rate

📈 Data Visualization

The application includes visualizations such as:

Views by Video
Likes by Video
Views vs Engagement Rate
Top Videos by Engagement Rate
Sentiment Distribution

😊 Sentiment Analysis

Video titles are analyzed and categorized into:

Positive
Neutral
Negative

🔍 Video Filtering

Users can filter videos based on:

Sentiment
Minimum Views

↕️ Video Sorting

Videos can be sorted based on different performance metrics such as:

Views
Likes
Comments
Engagement Rate

🎥 Video Viewer

Users can select a video from the search results and watch it directly within the application.

📥 Download Results

Users can download:

Filtered video results as CSV
Analytics summary

🛠️ Technologies Used
Python
Streamlit
Pandas
Plotly
YouTube Data API
TextBlob
python-dotenv

📁 Project Structure

youtube-search-analyzer/
│
├── assets/
│
├── data/
│   ├── cleaned_videos.csv
│   └── videos.csv
│
├── screenshots/
│
├── .env
├── .gitignore
├── analysis.py
├── api.py
├── app.py
├── README.md
├── requirements.txt
├── sentiment.py
└── visualization.py

⚙️ Installation

1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate to the project folder
cd youtube-search-analyzer

3. Create a virtual environment
python -m venv venv

4. Activate the virtual environment
Windows
venv\Scripts\activate

5. Install dependencies
pip install -r requirements.txt

🔑 API Configuration

Create a .env file in the project directory.

Add your YouTube API key:

YOUTUBE_API_KEY=your_api_key_here

⚠️ Important: Never upload your .env file or API key to GitHub.

The .gitignore file is configured to prevent sensitive files from being uploaded.

▶️ Run the Application

Start the Streamlit application using:

streamlit run app.py

The application will open in your browser.

📊 Example Analysis

For a search such as:

Data Analytics

the application can provide:

Total number of videos returned
Total views
Total likes
Average engagement
Most viewed video
Most liked video
Highest engagement video
Sentiment distribution
Top videos by engagement

💡 Key Insights

The dashboard helps users identify:

Which videos receive the highest number of views.
Which videos generate the most likes.
Which videos have higher engagement rates.
How video titles are distributed across sentiment categories.
Which videos perform well based on selected filters.
How views relate to engagement.

🎯 Project Objective

The main objective of this project is to demonstrate how Python-based data analytics can be used to collect, clean, analyze, visualize, and interpret YouTube video performance data.

📌 Future Improvements

Possible future enhancements include:

Channel-level performance analysis
Trending topic detection
Keyword analysis
Time-series analysis
Thumbnail analysis
Advanced NLP analysis
Competitor/channel comparison
Additional YouTube metrics
Deployment using Streamlit Cloud

## 👨‍💻 Author
Ezhilvendhan P
MBA – Data Analytics

⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.