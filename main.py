import streamlit as st
import requests
import datetime

#input=========================================
url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"
date = st.date_input("Enter Date: ")

#Get info=========================================
def fetch_info(date):
    NewUrl = url + "/" + str(date).replace("-", "")[2:]
    r = requests.get(f"{NewUrl}")
    if NewUrl["status"] != 404:
        r.raise_for_status()
        return r.json()
    else:
        return False

result = fetch_info(date)

#display=========================================
st.write(result)
st.write(result["title"])