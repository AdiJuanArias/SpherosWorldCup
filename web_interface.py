import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from img_recognitizon import get_coords


sphero_coords, obstacle_coords = get_coords('pixel.jepg')

map_data = sphero_coords + obstacle_coords
x_coords = [coord[0] for coord in map_data]
y_coords = [coord[1] for coord in map_data]




st.title("Welcome to Spheros World Cup")

st.sidebar.header("Spheros World Cup")

# If the user selects "View teams", show a list of all the teams in the tournament.
#if st.sidebar.checkbox("View teams"):
  #st.table(data=[[team.name, team.country] for team in teams])

# If the user selects "View matches", show a list of all the matches in the tournament.
#if st.sidebar.checkbox("View matches"):
  #st.table(data=[[match.home_team, match.away_team, match.date, match.time] for match in matches])

# Show map
map_container = st.container()

with map_container:
    fig = px.scatter(x_coords, y_coords)
    st.plotly_chart(fig, use_container_width=True)