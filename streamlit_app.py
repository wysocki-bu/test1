import streamlit as st
import pandas as pd
import numpy as np

# Title for graph
st.write("# BA870-Simple StreamLit App")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Americas Net Income", "Europe Net Income", "Asia Net Income"])

# Graph data
st.bar_chart(chart_data)
