# import libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.set_page_config(
    page_title="Team Analysis",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊",
)

st.title("Team Analysis")

# Load data
df = pd.read_csv("cleaned_soccer.csv")

# sidebar
st.sidebar.subheader("Choose Your Favorite Team")

# Filters
leage_country_filter = st.sidebar.selectbox(
    "Type of filter League/Country", ["league", "country"]
)
leage_country_name = st.sidebar.selectbox(
    "Select League/Country name", list(df[leage_country_filter].unique())
)
team_filter = st.sidebar.selectbox(
    "Select Team",
    list(df[df[leage_country_filter] == leage_country_name]["team_name"].unique()),
)
seasons = list(df["season"].unique())
seasons.sort()
season_filter = st.sidebar.selectbox(
    "Select Season",
    seasons,
)

# Body

# Matrix
st.subheader(f"{team_filter} from 2008 to 2016")

col1, col2, col3, col4, col5 = st.columns(5)  # For Horizontal matrix
col1.metric(
    "Total Scored Goals", df.loc[df["team_name"] == team_filter]["team_goals"].sum()
)
col2.metric(
    "Total Achieved Points", df.loc[df["team_name"] == team_filter]["points"].sum()
)
col3.metric(
    "Total Wins",
    df.loc[df["team_name"] == team_filter]["result"].value_counts()["won"],
)
col4.metric(
    "Total Loses",
    df.loc[df["team_name"] == team_filter]["result"].value_counts()["lost"],
)
col5.metric(
    "Total Draws",
    df.loc[df["team_name"] == team_filter]["result"].value_counts()["draw"],
)

# Team Goals and Points Over Seasons Lines Subplots
team_goals = dict(
    df.loc[df["team_name"] == team_filter].groupby("season")["team_goals"].sum()
)

team_points = dict(
    df.loc[df["team_name"] == team_filter].groupby("season")["points"].sum()
)

fig = make_subplots(rows=2, cols=1, subplot_titles=("Goals", "Points"))
fig.append_trace(
    go.Scatter(
        x=list(team_goals.keys()),
        y=list(team_goals.values()),
    ),
    row=1,
    col=1,
)

fig.append_trace(
    go.Scatter(
        x=list(team_points.keys()),
        y=list(team_points.values()),
    ),
    row=2,
    col=1,
)

fig.update_layout(
    height=600, width=600, title_text=f"{team_filter} Goals and Points Over Seasons"
)
st.plotly_chart(fig, use_container_width=True)

# row 2
c1, c2, c3 = st.columns((3, 3, 4))
with c1:
    # Team results at home
    home_team_results = df[
        (df["team_name"] == team_filter) & (df["Home/Away"] == "home_team")
    ]["result"].value_counts()
    fig_home_team_results = px.pie(
        values=home_team_results,
        names=home_team_results.index,
        title=f"{team_filter} Team results at home",
    )
    st.plotly_chart(fig_home_team_results, use_container_width=True)
with c2:
    # Team away results
    away_team_results = df[
        (df["team_name"] == team_filter) & (df["Home/Away"] == "away_team")
    ]["result"].value_counts()
    fig_away_team_results = px.pie(
        values=away_team_results,
        names=away_team_results.index,
        title=f"{team_filter} Team away results",
    )
    st.plotly_chart(fig_away_team_results, use_container_width=True)

with c3:
    team_formations = dict(
        df.loc[df["team_name"] == team_filter]["formation"].value_counts()
    )

    fig_team_formations = px.bar(
        x=team_formations.keys(),
        y=team_formations.values(),
        title=f"{team_filter} Team Formations",
        color=team_formations.keys(),
        labels={"x": "Formation", "y": "Counts"},
    )
    st.plotly_chart(fig_team_formations, use_container_width=True)


# row 3
st.subheader(f"Season {season_filter}")

d1, d2, d3 = st.columns((3, 3, 4))
with d1:
    # Team results at home
    home_team_results = df[
        (df["team_name"] == team_filter)
        & (df["Home/Away"] == "home_team")
        & (df["season"] == season_filter)
    ]["result"].value_counts()
    fig_home_team_results = px.pie(
        values=home_team_results,
        names=home_team_results.index,
        title=f"{team_filter} Team results at home",
        hole=0.4,
    )
    st.plotly_chart(fig_home_team_results, use_container_width=True)
with d2:
    # Team away results
    away_team_results = df[
        (df["team_name"] == team_filter)
        & (df["Home/Away"] == "away_team")
        & (df["season"] == season_filter)
    ]["result"].value_counts()
    fig_away_team_results = px.pie(
        values=away_team_results,
        names=away_team_results.index,
        title=f"{team_filter} Team away results",
        hole=0.4,
    )
    st.plotly_chart(fig_away_team_results, use_container_width=True)

with d3:
    team_formations = dict(
        df.loc[(df["team_name"] == team_filter) & (df["season"] == season_filter)][
            "formation"
        ].value_counts()
    )

    fig_team_formations = px.bar(
        x=team_formations.keys(),
        y=team_formations.values(),
        title=f"{team_filter} Team Formations",
        color=team_formations.keys(),
        labels={"x": "Formation", "y": "Counts"},
    )
    st.plotly_chart(fig_team_formations, use_container_width=True)

# Season Details
btn = st.button("Display Season Details")
if btn:
    st.dataframe(
        df[(df["team_name"] == "Manchester United") & (df["season"] == "2015/2016")][
            ["stage", "Home/Away", "team_goals", "result", "formation", "date"]
        ].sort_values(by=["stage"]),
        use_container_width=True,
    )
