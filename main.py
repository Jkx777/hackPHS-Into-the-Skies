import streamlit as st
import requests
import datetime

url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"
date = st.date_input("Enter Date: ")

def fetch_info(date):
    NewUrl = url + "/" + str(date).replace("-", "")[2:]
    r = requests.get(f"{NewUrl}")
    st.write(r)
    if r == 200:
        r.raise_for_status()
        return r.json()
    else:
        return False

result = fetch_info(date)
st.write(result)
st.write(result["title"])