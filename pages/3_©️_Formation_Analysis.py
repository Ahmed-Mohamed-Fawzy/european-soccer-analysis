# import libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.set_page_config(
    page_title="Formation Analysis",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="©️",
)

st.title("Formation Analysis")

# Load data
df = pd.read_csv("cleaned_soccer.csv")


# sidebar

# Filters


# Body

# Matrix
st.subheader("Most Frequently Used Formation")

col1, col2, col3 = st.columns(3)  # For Horizontal matrix
col1.metric("Overall", df["formation"].mode()[0])
col2.metric(
    "Home Team",
    df.loc[df["Home/Away"] == "home_team"]["formation"].mode()[0],
)
col3.metric(
    "Away Team",
    df.loc[df["Home/Away"] == "away_team"]["formation"].mode()[0],
)


# Bar chart Most Frequently Used Formations per Season
season_list = df["season"].unique().tolist()
season_list.sort()

dict_season = dict(df.groupby(["season"])["formation"].agg(pd.Series.mode))


dict_season_freq = {}
for item in season_list:
    freq = df.groupby(["season"])["formation"].value_counts()[item][0]
    dict_season_freq[item] = freq

fig = px.bar(
    x=list(dict_season.keys()),
    y=list(dict_season_freq.values()),
    text=list(dict_season.values()),
    color=list(dict_season.keys()),
    title="Most Frequently Used Formations per Season",
    labels={"x": "Season", "y": "Formation"},
)
st.plotly_chart(fig, use_container_width=True)


# row 2
c1, c2 = st.columns((1, 1))
with c1:
    # Horizontal Bar chart
    home_formations = dict(
        df.loc[df["Home/Away"] == "home_team"]["formation"].value_counts()
    )
    home_formations = sorted(home_formations.items(), key=lambda x: x[1])
    home_formations = dict(home_formations)

    fig_home_formations = px.bar(
        x=home_formations.values(),
        y=home_formations.keys(),
        title="Home Team Formations Usage",
        color=home_formations.keys(),
        labels={"x": "Counts", "y": "Formation"},
    )
    st.plotly_chart(fig_home_formations, use_container_width=True)

with c2:
    # Horizontal Bar chart
    away_formations = dict(
        df.loc[df["Home/Away"] == "away_team"]["formation"].value_counts()
    )
    away_formations = sorted(away_formations.items(), key=lambda x: x[1])
    away_formations = dict(away_formations)

    fig_away_formations = px.bar(
        x=away_formations.values(),
        y=away_formations.keys(),
        title="Away Team Formations Usage",
        color=away_formations.keys(),
        labels={"x": "Counts", "y": "Formation"},
    )
    st.plotly_chart(fig_away_formations, use_container_width=True)

# most used formation per leagues
dict_leagues = dict(df.groupby(["league"])["formation"].agg(pd.Series.mode))
dict_leagues_freq = {}
for item in list(dict_leagues.keys()):
    freq = df.groupby(["league"])["formation"].value_counts()[item][0]
    dict_leagues_freq[item] = freq

fig_league = px.bar(
    x=list(dict_leagues.keys()),
    y=list(dict_leagues_freq.values()),
    text=list(dict_leagues.values()),
    color=list(dict_leagues.keys()),
    title="Most Frequently used Formations per league",
    labels={"x": "league", "y": "formation"},
)
st.plotly_chart(fig_league, use_container_width=True)
