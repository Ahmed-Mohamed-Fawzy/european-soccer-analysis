# import libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from collections import OrderedDict

st.set_page_config(
    page_title="Overall Analysis",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🥇",
)

st.title("Overall Analysis")

# Load data
df = pd.read_csv("cleaned_soccer.csv")

# sidebar
st.sidebar.subheader("Choose Your Favorite Team")

# Filters
seasons = list(df["season"].unique())
seasons.sort()
season_filter = st.sidebar.selectbox(
    "Select Season",
    seasons,
)

# Body
match_counts_dict = dict(df["season"].value_counts() / 2)
sorted_dict = OrderedDict(sorted(match_counts_dict.items()))
fig = px.bar(
    x=sorted_dict.keys(),
    y=list(sorted_dict.values()),
    text=list(sorted_dict.values()),
    color=list(sorted_dict.keys()),
    title="Match Counts",
    labels={"x": "Season", "y": "Number of Matches"},
)
st.plotly_chart(fig, use_container_width=True)

# Top 10 Goal Scorrer Teams per season
top_10_scorrer = (
    df[df["season"] == season_filter].groupby("team_name")["team_goals"].sum()
)
top_10_scorrer.sort_values(ascending=False, inplace=True)
top_10_scorrer = dict(top_10_scorrer[0:10])

fig_top_10_scorrer = px.bar(
    x=top_10_scorrer.keys(),
    y=list(top_10_scorrer.values()),
    text=list(top_10_scorrer.values()),
    color=list(top_10_scorrer.keys()),
    title=f"Top 10 Goal Scorerr Teams for {season_filter}",
    labels={"x": "", "y": "Goals"},
)
st.plotly_chart(fig_top_10_scorrer, use_container_width=True)

# Leages Goals for season
leagues_goals = df[df["season"] == season_filter].groupby("league")["team_goals"].sum()
leagues_goals.sort_values(ascending=False, inplace=True)
leagues_goals = dict(leagues_goals[0:10])

fig_leagues_goals = px.bar(
    x=leagues_goals.keys(),
    y=list(leagues_goals.values()),
    text=list(leagues_goals.values()),
    color=list(leagues_goals.keys()),
    title=f"Leagues Goals for {season_filter}",
    labels={"x": "", "y": "Goals"},
)
st.plotly_chart(fig_leagues_goals, use_container_width=True)
