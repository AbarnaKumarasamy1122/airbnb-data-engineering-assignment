
import streamlit as st
import pandas as pd

df = pd.read_csv("airbnb_master_table.csv")

st.title("Airbnb Market Intelligence Dashboard")

st.write("Dataset Overview")

st.dataframe(df.head())
