import streamlit as st
import pandas as pd
from io import StringIO
import os 
import time


st. set_page_config(layout="wide")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    st.image(uploaded_file)
    with open(os.path.join("tmp",str(time.time()+".png")),"wb") as f: 
        f.write(uploaded_file.getbuffer())         
    st.success("Saved File")


import numpy as np

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)