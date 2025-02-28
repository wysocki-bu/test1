import streamlit as st
import pandas as pd
import numpy as np

st.write("# Simple StreamLit App: Graph of Global Net Income")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Americas NetIncome", "Europe Net Income", "Asia Net Income"])

st.bar_chart(chart_data)
