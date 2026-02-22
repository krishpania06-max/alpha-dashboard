import streamlit as st
import pandas as pd
import numpy as np

# Set the page config to have the title and the layout
st.set_page_config(page_title="Alpha Dashboard", layout="wide")

# Title and header
st.title("Alpha Dashboard")
st.header("Welcome to the Bloomberg-style Dashboard")

# Simulated stock data
numbers = np.random.randn(100)
df = pd.DataFrame({"Stock Prices": numbers})

# Display data and charts
st.subheader("Stock Price Trend")
st.line_chart(df)

# Sidebar for controls
st.sidebar.header("Control Panel")
selected_stock = st.sidebar.selectbox("Select a Stock", ["AAPL", "GOOGL", "MSFT"])
st.write(f"You selected: {selected_stock}")

# Display more widgets or data as needed
