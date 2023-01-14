import streamlit as st
# Plotly - data vizualization library (like Bokeh)
import plotly.express as px
from functions import get_data

# Order of code defines order of widgets on the webpage
st.title("Weather Forecast")
place = st.text_input("Place: ", value = "London")
# creates slider
number_of_days = st.slider("Forecast Days", min_value = 1, max_value =5,
                           help = "Select the number of forecasted days")
# creates select box
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
if number_of_days>1:
    day_or_days = "days"
elif number_of_days ==1:
    day_or_days = "day"
st.subheader(f"{option} for the next {number_of_days} {day_or_days} in {place}")

try:
    # Get Temperature or sky data
    filtered = get_data(place, number_of_days)

    if option == "Temperature":
        # Create a temperature plot
        temperatures = [dict["main"]["temp"] for dict in filtered]
        #temperatures = [temp-273.15 for temp in temperatures]
        dates = [dict["dt_txt"] for dict in filtered]
        figure = px.line(x=dates, y=temperatures, labels={"x":"Date", "y":"Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width =115)
except KeyError:
    st.write("You typed in invalid city, please type again.")