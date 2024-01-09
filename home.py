import os
import re
import streamlit as st
from functions.svg import cat, css

st.markdown(css, unsafe_allow_html=True)

st.markdown("### TOC:")

directory_path = "./pages"
file_list = os.listdir(directory_path)
for file in file_list:
    # Remove numbers and underscores from the beginning of the file name
    file_name = re.sub(r"^\d+_", "", file)
    # Remove the .py extension from the file name
    file_name = os.path.splitext(file_name)[0].capitalize().replace("_", " ")
    
    file_path = os.path.join(directory_path, file)
    file_url = f"[{file_name}]({file_path})"
    st.markdown(f"* {file_url}")

st.markdown(cat, unsafe_allow_html=True)