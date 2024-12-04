import streamlit as st
import pandas as pd
import numpy as np

# Title and description
st.title("Simple Streamlit App")
st.write("This is a demo app.")

# Create a sample dataframe
data = pd.DataFrame({
    'Column 1': np.random.randn(10),
    'Column 2': np.random.randn(10),
})

# Display the dataframe
st.write("Here is a sample DataFrame:")
st.dataframe(data)

# Add an interactive widget
st.write("Pick a number from the slider below:")
selected_number = st.slider("Choose a number", 0, 100)
st.write(f"You selected: {selected_number}")

# Add a chart
st.write("Here’s a line chart based on the data:")
st.line_chart(data)
