import os
import requests
import streamlit as st

API_HOST = os.getenv("API_HOST", "http://backend:8000")  # override in .env

st.title("Welcome to MyApp")

name = st.text_input("Enter your name (Try Bob or Alice, who exist in the database)", value="")
clicked = st.button("Go")

if clicked and name:
    try:
        resp = requests.get(f"{API_HOST}/hello/{name}", timeout=5)
        if resp.ok:
            st.success(resp.json()["message"])
        else:
            st.error(f"API error: {resp.status_code}, message: {resp.text}")
    except requests.RequestException as exc:
        st.error(f"Request failed: {exc}")
