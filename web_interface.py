import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from parameters_estimator import pix_to_cm, get_parameters
# from img_recognitizon import get_coords


st.title("Welcome to Spheros World Cup")

st.sidebar.header("Spheros World Cup")

# If the user selects "View teams", show a list of all the teams in the tournament.
# if st.sidebar.checkbox("View teams"):
# st.table(data=[[team.name, team.country] for team in teams])

# If the user selects "View matches", show a list of all the matches in the tournament.
# if st.sidebar.checkbox("View matches"):
# st.table(data=[[match.home_team, match.away_team, match.date, match.time] for match in matches])

# Show map
px_cm_cont = st.container()

with px_cm_cont:
    header = st.header("Cet Parameters for Sphero", divider="orange")
    st.markdown("""Put the coordinates of the point you want your sphero to go.
          This tool will transform your input to the needed parameters for your sphero's movements""")

    col1, col2 = st.columns(2)
    with col1:
        x_coord = st.number_input("Put the x coordinate", key="x", step=1)
    with col2:
        y_coord = st.number_input("Put the x coordinate", key="y", step=1)
    
    distance, angle, time = get_parameters(x_coord, y_coord)

col1_result, col2_result, col3_result = st.columns(3)

with col1_result:
    distance_metric = st.metric(label="Distance", value=str(distance) + " cm", help= "Minimum distance between your sphero and the coordinate")
with col2_result:
    angle_metric = st.metric(label="Angle", value=str(angle) + " °", help= "complete this")
with col3_result:
    time_metric = st.metric(label="Time", value=str(time) + " s", 
    help= "The time your sphero should take to go to the destination at a constant speed")