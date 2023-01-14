import streamlit as st
# Plotly - data vizualization library (like Bokeh)
import plotly.express as px
from functions import get_data

# Order of code defines order of widgets on the webpage
st.title("Weather Forecast")
place = st.text_input("Place: ")
# creates slider
days = st.slider("Forecast Days", min_value = 1, max_value =5,
                 help = "Select the number of forecasted days")
# creates select box
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
d,t = get_data(place, days, option)

figure = px.line()
st.plotly_chart()