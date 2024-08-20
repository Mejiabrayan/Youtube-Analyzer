"""
@author: Brayan
"""

import pandas as pd
import streamlit as st
import plotly.express as px

# import plotly.graph_objects as go

# Configure Streamlit page
st.set_page_config(page_title="YouTube Analytics Dashboard", layout="wide")


# Load Data
@st.cache_data
def load_data():
    df_agg = pd.read_csv("Aggregated_Metrics_By_Video.csv").iloc[1:, :]
    df_agg_sub = pd.read_csv("Aggregated_Metrics_By_Country_And_Subscriber_Status.csv")
    df_comments = pd.read_csv("All_Comments_Final.csv")
    df_time = pd.read_csv("Video_Performance_Over_Time.csv")
    df_time["Date"] = pd.to_datetime(df_time["Date"], format="mixed")  # Updated line
    return df_agg, df_agg_sub, df_comments, df_time


# We're loading the data here
df_agg, df_agg_sub, df_comments, df_time = load_data()
print("HERE IS THE TIME", df_time.columns)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Video Performance", "Audience Insights"])

if page == "Overview":
    st.title("YouTube Analytics Dashboard")
    st.header("Overview")

    # Display key metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Views", df_agg["Views"].sum())
    col2.metric("Total Likes", df_agg["Likes"].sum())
    col3.metric("Total Comments", df_comments.shape[0])

    # Display the DataFrame in Streamlit
    st.subheader("Aggregated Metrics by Video")
    st.dataframe(df_agg)


elif page == "Video Performance":
    st.title("Video Performance")

    # Top 10 videos by views
    top_10_videos = df_agg.nlargest(10, "Views")
    fig_top_10 = px.bar(
        top_10_videos, x="Video title", y="Views", title="Top 10 Videos by Views"
    )
    st.plotly_chart(fig_top_10)

    # Views vs. Likes scatter plot
    fig_scatter = px.scatter(
        df_agg,
        x="Views",
        y="Likes",
        hover_name="Video title",
        title="Views vs. Likes for Each Video",
    )
    st.plotly_chart(fig_scatter)

    # Video performance over time
    video_select = st.selectbox("Select a video:", df_time["Video Title"].unique())

    video_data = df_time[df_time["Video Title"] == video_select]

    fig_time = px.line(
        video_data,
        x="Date",
        y="Views",
        title=f"Performance Over Time: {video_select}",
    )
    st.plotly_chart(fig_time)

elif page == "Audience Insights":
    st.title("Audience Insights")

    # Subscriber vs. Non-Subscriber views
    sub_data = df_agg_sub.groupby("Is Subscribed")["Views"].sum().reset_index()
    fig_pie = px.pie(
        sub_data,
        values="Views",
        names="Is Subscribed",
        title="Subscriber vs. Non-Subscriber Views",
    )
    st.plotly_chart(fig_pie)

    # Top 10 countries by views
    top_countries = (
        df_agg_sub.groupby("Country Code")["Views"].sum().nlargest(10).reset_index()
    )
    fig_countries = px.bar(
        top_countries, x="Country Code", y="Views", title="Top 10 Countries by Views"
    )
    st.plotly_chart(fig_countries)

    # Comment sentiment analysis (assuming you have sentiment scores)
    if "Sentiment" in df_comments.columns:
        sentiment_counts = df_comments["Sentiment"].value_counts()
        fig_sentiment = px.pie(
            sentiment_counts,
            values=sentiment_counts.values,
            names=sentiment_counts.index,
            title="Comment Sentiment Analysis",
        )
        st.plotly_chart(fig_sentiment)
    else:
        st.write("Sentiment analysis data not available")

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Dashboard created by Brayan")
