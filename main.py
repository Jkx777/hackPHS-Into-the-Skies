import streamlit as st
import requests
import datetime

st.title("Into the Skies")
#input=========================================
url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"
date = st.date_input("Enter Date: ")

#Get info=========================================
def fetch_info(date):
    NewUrl = url + "/" + str(date).replace("-", "")[2:]
    r = requests.get(f"{NewUrl}")
    r.raise_for_status()
    return r.json()

result = fetch_info(date)
#st.write(result)

#display=========================================
st.subheader(result["title"])
st.image(result["hdurl"])
st.html(result["explanation"])


