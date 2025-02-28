import streamlit as st
import pandas as pd
import numpy as np

st.write("# Simple StreamLit App: Graph Sales")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)

# Create a sample dataframe
#data = pd.DataFrame({
#  'Year': [2018, 2019, 2020, 2021],
#  'Sales': [350, 480, 550, 680]
#})
 
# Create a line chart
#st.line_chart(data)
