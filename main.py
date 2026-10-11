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
    status = r.raise_for_status()
    st.write(status)
    if status == 200:
        return r.json()
    else:
        return False

result = fetch_info(date)

#display=========================================
if result == False:
    st.subheader("Enter a different date")
else:
    st.subheader(result["title"])
    image, info = st.columns(2)

    with image:
        st.image(result["hdurl"])

    with info:
        st.html(result["explanation"])