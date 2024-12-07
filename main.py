import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.read_csv('iris.csv')

st.scatter_chart(chart_data)