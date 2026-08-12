import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import plotly.express as px
from sentiment import add_sentiment
from api import search_youtube


# =========================================================
# LOAD API KEY
# =========================================================

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="YouTube Search Analyzer",
    page_icon="🎬",
    layout="wide"
)


# =========================================================
# TITLE
# =========================================================

st.title("🎬 YouTube Search Analyzer")

st.write(
    "Search YouTube videos and analyze views, likes, comments and engagement."
)


# ============================================================
# SIDEBAR - SEARCH CONTROLS
# ============================================================

with st.sidebar:

    st.header("🔎 Search Controls")

    search_query = st.text_input(
        "Search YouTube",
        placeholder="Example: Data Analytics"
    )

    num_results = st.slider(
        "Number of videos",
        min_value=5,
        max_value=50,
        value=20
    )

    search_button = st.button(
        "🔍 Search YouTube",
        use_container_width=True
    )


# =========================================================
# SEARCH BUTTON
# =========================================================

if search_button:

    if not API_KEY:

        st.error(
            "YouTube API key was not found in your .env file."
        )

    elif not search_query:

        st.warning(
            "Please enter a search topic."
        )

    else:

        with st.spinner("Searching YouTube..."):

            df = search_youtube(
                search_query,
                num_results
            )

        st.write(
            "Videos returned:",
            len(df)
        )

        if df.empty:

            st.warning(
                "No videos found."
            )

            # Remove old results
            if "df" in st.session_state:
                del st.session_state["df"]

        else:

            # =================================================
            # CALCULATE ENGAGEMENT RATE
            # =================================================

            df["engagement_rate"] = (
                (
                    df["likes"] +
                    df["comments"]
                )
                / df["views"].replace(0, 1)
            ) * 100


            # =================================================
            # SENTIMENT ANALYSIS
            # =================================================

            df = add_sentiment(
                df,
                "title"
            )


            # =================================================
            # SAVE DATAFRAME
            # =================================================

            st.session_state["df"] = df


# =========================================================
# DISPLAY RESULTS ONLY AFTER SEARCH
# =========================================================

if "df" in st.session_state:

    df = st.session_state["df"].copy()

    if not df.empty:

        # ==============================
        # KPI DASHBOARD
        # ==============================

        st.subheader("📊 Performance Overview")

        total_views = df["views"].sum()
        total_likes = df["likes"].sum()
        total_comments = df["comments"].sum()
        avg_engagement = df["engagement_rate"].mean()

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "🎬 Videos",
                f"{len(df):,}"
            )

        with col2:
            st.metric(
                "👀 Total Views",
                f"{total_views:,}"
            )

        with col3:
            st.metric(
                "👍 Total Likes",
                f"{total_likes:,}"
            )

        with col4:
            st.metric(
                "📈 Avg. Engagement",
                f"{avg_engagement:.2f}%"
            )

        st.divider()


        # =====================================================
        # RESULTS TABLE
        # =====================================================

        st.subheader(
            "📊 YouTube Search Results"
        )

        st.dataframe(
            df,
            column_config={
                "video_url": st.column_config.LinkColumn(
                    "YouTube Video",
                    display_text="▶️ Watch Video"
                )
            },
            hide_index=True,
            width="stretch"
        )


        # =====================================================
        # WATCH VIDEO
        # =====================================================

        st.subheader(
            "▶️ Watch Video"
        )

        video_options = dict(
            zip(
                df["title"],
                df["video_url"]
            )
        )

        selected_video = st.selectbox(
            "Select a video to watch:",
            list(video_options.keys())
        )

        if selected_video:

            st.video(
                video_options[selected_video]
            )


       # Views chart

        st.subheader("👀 Views by Video")

        views_df = df.sort_values(
            by="views",
            ascending=True
        )

        fig_views = px.bar(
            views_df,
            x="views",
            y="title",
            orientation="h",
            text="views",
            title="Views by Video",
            labels={
                "views": "Views",
                "title": "Video"
            }
        )

        fig_views.update_traces(
            texttemplate="%{text:,}",
            textposition="outside"
        )

        fig_views.update_layout(
            height=500,
            xaxis_title="Views",
            yaxis_title=""
        )

        st.plotly_chart(
            fig_views,
            use_container_width=True
        )
        # =====================================================
        # LIKES CHART
        # =====================================================

        
        st.subheader("👍 Likes by Video")

        likes_df = df.sort_values(
            by="likes",
            ascending=True
        )

        fig_likes = px.bar(
            likes_df,
            x="likes",
            y="title",
            orientation="h",
            text="likes",
            title="Likes by Video",
            labels={
                "likes": "Likes",
                "title": "Video"
            }
        )

        fig_likes.update_traces(
            texttemplate="%{text:,}",
            textposition="outside"
        )

        fig_likes.update_layout(
            height=500,
            xaxis_title="Likes",
            yaxis_title=""
        )

        st.plotly_chart(
            fig_likes,
            use_container_width=True
        )


        # Views vs Engagement Analysis
       
        st.subheader("📈 Views vs Engagement Rate")

        scatter_df = df[
            ["title", "views", "likes", "comments", "engagement_rate"]
        ].copy()

        fig_scatter = px.scatter(
            scatter_df,
            x="views",
            y="engagement_rate",
            hover_name="title",
            hover_data={
                "views": ":,",
                "likes": ":,",
                "comments": ":,",
                "engagement_rate": ":.2f"
            },
            title="Views vs Engagement Rate",
            labels={
                "views": "Views",
                "engagement_rate": "Engagement Rate (%)",
                "likes": "Likes",
                "comments": "Comments"
            }
        )

        fig_scatter.update_traces(
            marker_size=12,
            hovertemplate=(
                "<b>%{hovertext}</b><br>"
                "Views: %{x:,}<br>"
                "Engagement Rate: %{y:.2f}%<br>"
                "<extra></extra>"
            )
        )

        fig_scatter.update_layout(
            height=500,
            xaxis_title="Views",
            yaxis_title="Engagement Rate (%)"
        )

        st.plotly_chart(
            fig_scatter,
            use_container_width=True
        )

        # =====================================================
        # FILTER VIDEOS
        # =====================================================
        
        st.subheader("🔍 Filter Videos")

        filter_col1, filter_col2 = st.columns([1, 1])

        with filter_col1:
            sentiment_filter = st.selectbox(
                "😊 Filter by Sentiment",
                ["All", "Positive", "Neutral", "Negative"]
            )

        with filter_col2:
            min_views = st.number_input(
                "👀 Minimum Views",
                min_value=0,
                value=0,
                step=1000
            )

        # Start with all videos
        filtered_df = df.copy()

        # Apply sentiment filter
        if sentiment_filter != "All":
            filtered_df = filtered_df[
                filtered_df["sentiment"] == sentiment_filter
            ]

        # Apply minimum views filter
        filtered_df = filtered_df[
            filtered_df["views"] >= min_views
        ]

        st.write(
            f"Showing **{len(filtered_df)}** of **{len(df)}** videos"
        )
     

        # =====================================================
        # FILTERED RESULTS
        # =====================================================

        st.dataframe(
            filtered_df,
            column_config={
                "video_url": st.column_config.LinkColumn(
                    "YouTube Video",
                    display_text="▶️ Watch Video"
                )
            },
            hide_index=True,
            width="stretch"
        )


        # =====================================================
        # DOWNLOAD FILTERED RESULTS
        # =====================================================

        st.subheader("📥 Download Results")

        # CSV download
        csv = filtered_df.to_csv(index=False)

        st.download_button(
            label="📥 Download Filtered Results (CSV)",
            data=csv,
            file_name="youtube_filtered_results.csv",
            mime="text/csv"
        )

        # Analytics summary
        summary_df = pd.DataFrame({
            "Metric": [
                "Total Videos",
                "Total Views",
                "Total Likes",
                "Total Comments",
                "Average Views",
                "Average Likes",
                "Average Comments",
                "Average Engagement Rate"
            ],
            "Value": [
                len(filtered_df),
                filtered_df["views"].sum(),
                filtered_df["likes"].sum(),
                filtered_df["comments"].sum(),
                round(filtered_df["views"].mean(), 2),
                round(filtered_df["likes"].mean(), 2),
                round(filtered_df["comments"].mean(), 2),
                round(filtered_df["engagement_rate"].mean(), 2)
            ]
        })

        summary_csv = summary_df.to_csv(index=False)

        st.download_button(
            label="📊 Download Analytics Summary",
            data=summary_csv,
            file_name="youtube_analytics_summary.csv",
            mime="text/csv"
        )


        # ============================================================
        # KEY INSIGHTS
        # ============================================================

        st.subheader("🏆 Key Insights")

        if not filtered_df.empty:

            # Basic calculations
            total_videos = len(filtered_df)

            avg_views = filtered_df["views"].mean()
            avg_likes = filtered_df["likes"].mean()
            avg_comments = filtered_df["comments"].mean()
            avg_engagement = filtered_df["engagement_rate"].mean()

            most_viewed = filtered_df.loc[
                filtered_df["views"].idxmax()
            ]

            most_liked = filtered_df.loc[
                filtered_df["likes"].idxmax()
            ]

            highest_engagement = filtered_df.loc[
                filtered_df["engagement_rate"].idxmax()
            ]

            # Average KPI metrics
            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "🎬 Videos",
                total_videos
            )

            col2.metric(
                "👀 Avg Views",
                f"{avg_views:,.0f}"
            )

            col3.metric(
                "👍 Avg Likes",
                f"{avg_likes:,.0f}"
            )

            col4.metric(
                "📈 Avg Engagement",
                f"{avg_engagement:.2f}%"
            )

            st.divider()

            # Top-performing videos
            st.markdown("### 🌟 Top Performing Videos")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.info(
                    f"👀 **Most Viewed**\n\n"
                    f"{most_viewed['title']}\n\n"
                    f"**{most_viewed['views']:,} views**"
                )

            with col2:
                st.info(
                    f"👍 **Most Liked**\n\n"
                    f"{most_liked['title']}\n\n"
                    f"**{most_liked['likes']:,} likes**"
                )

            with col3:
                st.info(
                    f"📈 **Highest Engagement**\n\n"
                    f"{highest_engagement['title']}\n\n"
                    f"**{highest_engagement['engagement_rate']:.2f}%**"
                )

        else:

            st.warning("No videos match the selected filters.")

    # ============================================================
    # TOP 5 VIDEOS BY ENGAGEMENT
    # ============================================================

    st.subheader("🏆 Top 5 Videos by Engagement")

    top_5 = filtered_df.sort_values(
        by="engagement_rate",
        ascending=False
    ).head(5)

    # Create horizontal chart
    fig_top5 = px.bar(
        top_5,
        x="engagement_rate",
        y="title",
        orientation="h",
        text="engagement_rate",
        title="Top 5 Videos by Engagement Rate",
        labels={
            "engagement_rate": "Engagement Rate (%)",
            "title": "Video"
        }
    )

    fig_top5.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig_top5.update_layout(
        height=500,
        xaxis_title="Engagement Rate (%)",
        yaxis_title="",
        yaxis={
            "categoryorder": "total ascending"
        }
    )

    st.plotly_chart(
        fig_top5,
        use_container_width=True
    )

    # ============================================================
    # CHANNEL PERFORMANCE ANALYSIS
    # ============================================================
    
    st.subheader("📺 Channel Performance Analysis")

    channel_df = (
        df.groupby("channel")
        .agg(
            Videos=("video_id", "count"),
            Total_Views=("views", "sum"),
            Total_Likes=("likes", "sum"),
            Total_Comments=("comments", "sum"),
            Avg_Engagement=("engagement_rate", "mean")
        )
        .reset_index()
    )

    channel_df["Avg_Engagement"] = (
        channel_df["Avg_Engagement"].round(2)
    )

    channel_df = channel_df.sort_values(
        by="Total_Views",
        ascending=False
    )

    st.dataframe(
        channel_df,
        hide_index=True,
        use_container_width=True
    )  
    st.subheader("👀 Total Views by Channel")

    channel_chart = channel_df.set_index("channel")[["Total_Views"]]

    st.bar_chart(channel_chart)


    # =====================================================
    # SENTIMENT ANALYSIS
    # =====================================================

    st.subheader(
        "😊 Sentiment Analysis"
    )


    sentiment_counts = (
        df["sentiment"]
        .value_counts()
        .reindex(
            ["Positive", "Neutral", "Negative"],
            fill_value=0
        )
    )

    positive_count = sentiment_counts.get(
        "Positive",
        0
    )

    neutral_count = sentiment_counts.get(
        "Neutral",
        0
    )

    negative_count = sentiment_counts.get(
        "Negative",
        0
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "😊 Positive",
            positive_count
        )


    with col2:

        st.metric(
            "😐 Neutral",
            neutral_count
        )


    with col3:

        st.metric(
            "😞 Negative",
            negative_count
        )


    # Sentiment chart
    # Prepare sentiment data for chart
    sentiment_counts = df["sentiment"].value_counts()

    sentiment_df = sentiment_counts.reindex(
        ["Positive", "Neutral", "Negative"],
        fill_value=0
    ).reset_index()

    sentiment_df.columns = ["Sentiment", "Videos"]

    fig_sentiment = px.bar(
        sentiment_df,
        x="Sentiment",
        y="Videos",
        text="Videos",
        title="Video Sentiment Distribution",
        labels={
            "Sentiment": "Sentiment",
            "Videos": "Number of Videos"
        },
        category_orders={
            "Sentiment": ["Positive", "Neutral", "Negative"]
        }
    )

    fig_sentiment.update_traces(
        textposition="outside",
        textfont_size=16,
        hovertemplate="<b>%{x}</b><br>Videos: %{y}<extra></extra>"
    )

    fig_sentiment.update_layout(
        height=450,
        xaxis_title="",
        yaxis_title="Number of Videos",
        title_x=0,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(size=14),
        margin=dict(l=40, r=40, t=70, b=40)
    )

    st.plotly_chart(
        fig_sentiment,
        use_container_width=True
    )


    # =====================================================
    # SORTING
    # =====================================================

    st.subheader(
        "🔽 Sort YouTube Videos"
    )


    sort_by = st.selectbox(
        "Sort videos by:",
        [
            "Views",
            "Likes",
            "Comments",
            "Engagement Rate"
        ]
    )


    sort_columns = {
        "Views": "views",
        "Likes": "likes",
        "Comments": "comments",
        "Engagement Rate": "engagement_rate"
    }


    selected_column = sort_columns[
        sort_by
    ]


    sorted_df = filtered_df.sort_values(
        by=selected_column,
        ascending=False
    )


    st.dataframe(
        sorted_df,
        hide_index=True,
        width="stretch"
    )

   
   
# =========================================================
# BEFORE SEARCH
# =========================================================

else:

 st.info(
    "🔎 Enter a search topic above and click "
    "**Search YouTube** to analyze videos."
)