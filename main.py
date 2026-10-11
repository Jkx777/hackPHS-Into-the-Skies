import streamlit as st
import requests
import datetime
st.set_page_config(layout="wide")

st.title("Into the Skies")
st.write("==========================================================================================================================================")

#input=========================================
url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"
date = st.date_input("Enter Date: ")

#Get info=========================================
def fetch_info(date):
    NewUrl = url + "/" + str(date).replace("-", "")[2:]
    r = requests.get(f"{NewUrl}")
    if r.status_code == 200:
        r.raise_for_status()
        return r.json()
    else:
        return False

result = fetch_info(date)

#display=========================================
if result == False:
    col1, col2, col3 = st.columns([1, 20, 1])  # middle column is widest

    with col2:
        st.subheader("Please enter a different date.")
else:
    st.subheader(result["title"])
    image, info = st.columns(2)

    with image:
        st.image(result["hdurl"])

    with info:
        st.html(result["explanation"])