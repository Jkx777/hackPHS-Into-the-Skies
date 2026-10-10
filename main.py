import streamlit as st
import requests
import datetime

#inputs=====================================
url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"
date = st.date_input("Enter Date: ")

#Get info for specific date==========================
def fetch_info(date):
    if date in url:
        NewUrl = url + "/" + str(date).replace("-", "")[2:]
        r = requests.get(f"{NewUrl}")
        r.raise_for_status()
        return r.json()
    else:
        return "asdf"

result = fetch_info(date)

#display=====================================
st.write(result)
#st.title(result["title"])


