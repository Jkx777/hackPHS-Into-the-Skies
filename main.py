import streamlit as st
import requests
import datetime

#input=========================================
url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"
date = st.date_input("Enter Date: ")

#Get info=========================================
def fetch_info(date):
    comfirm = requests.get(f"{url}")#   \
    comfirm.raise_for_status()#          |  check later
    full = comfirm.json()#              /
    
    for i in range(len(full)):#             |
        dictionary = full[i]#               |
            if date in dictionary.values():#|
                NewUrl = url + "/" + str(date).replace("-", "")[2:]
                r = requests.get(f"{NewUrl}")
                r.raise_for_status()
                return r.json()
                break
            else:
                return "None"
                break
       
result = fetch_info(date)

#display=========================================
if result == "None":
    st.write("Please choose a different date")
else:
    st.write(result)
    st.write(result["title"])