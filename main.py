import requests
import streamlit as st

# Prepare the API key and API url
api_key = "VPIXkKf3JmUEbTG4LcduiwEVqaq2Keovw5x25MGS"
url = "https://api.nasa.gov/planetary/apod?api_key=VPIXkKf3JmUEbTG4LcduiwEVqaq2Keovw5x25MGS"


# Get the request data as a dictionary
request = requests.get(url)
content = request.json()

# Extract the image title, url and explanation
title = content["title"]
img_url = "https://api.nasa.gov/assets/img/general/apod.jpg"
explanation = content["explanation"]


# Download the image
image_filepath = "image.jpg"
response = requests.get(img_url)
with open(image_filepath, "wb") as file:
    file.write(response.content)

# Display on Streamlit Web App
st.title(title)
st.image(img_url)
st.write(explanation)


