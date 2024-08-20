# YouTube Analytics Dashboard

## Overview
The YouTube Analytics Dashboard is a web application built using Streamlit that provides insights into YouTube video performance and audience engagement. It allows users to visualize key metrics, analyze trends, and gain valuable insights from their YouTube data.

## Features
- **Overview Page**: Displays total views, likes, and comments.
- **Video Performance**: Visualizes top videos by views, views vs. likes scatter plot, and performance over time for selected videos.
- **Audience Insights**: Analyzes subscriber vs. non-subscriber views, top countries by views, and comment sentiment analysis.

## Technologies Used
- Python
- Streamlit
- Pandas
- Plotly

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Ensure you have the necessary CSV files in the project directory:
   - `Aggregated_Metrics_By_Video.csv`
   - `Aggregated_Metrics_By_Country_And_Subscriber_Status.csv`
   - `All_Comments_Final.csv`
   - `Video_Performance_Over_Time.csv`
   
2. Run the Streamlit app:
   ```bash
   streamlit run Dashboard.py
   ```

3. Open your web browser and go to `http://localhost:8501` to view the dashboard.
