# import libraries
import streamlit as st
from streamlit_lottie import st_lottie
import json
import pandas as pd
import numpy as np
import plotly.express as px


st.set_page_config(
    page_title="Home",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="⚽",
)

st.title("Main Page")

# Load data
df = pd.read_csv("cleaned_soccer.csv")


# sidebar
st.sidebar.header("European Soccer Analysis")
st.sidebar.image("image_tacticks.jpg")
st.sidebar.markdown(
    "Made By : [Ahmed Fawzy](https://www.linkedin.com/in/ahmedfawzy-ko/)"
)

# Body

# Animation upload and open
with open("animation.json") as source:
    animation = json.load(source)
st_lottie(animation)

# ABout Data section
st.subheader("About Dataset")
st.write("• Date: refers to the specific day on which a match was played.")
st.write("• Stage: every stage throughout the season.")
st.write("• Home/Away: identify if the match is on the home team or away.")
st.write("• Team goals: A goal set for the team for every match.")
st.write("• result: Team result for each match")
st.write(
    "• Points: refer to the number of points a team earns for each match they play."
)
st.write(
    "• Formation: refers to the way a soccer team is positioned on the field for each match."
)
st.write("• team_name: The complete name of the team.")
st.write("• league: refers to the league in which the team participates.")
st.write("• country: refers to the nation or geographical location of the team.")

btn = st.button("Display random samples")
if btn:
    st.write(df.sample(5))
