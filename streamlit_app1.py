"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np
# oneway -- 

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

#other way
dataframe = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))
st.dataframe(dataframe.style.highlight_max(axis=0))


# Draw a line chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

# Draw a Map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)


import streamlit as st
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'Qubed is', x * x * x)

# You can access the value at any point with:
st.text_input("Your name", key="name")
st.session_state.name

# use checkboxes to show/hide data
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(6, 3),
       columns=['a', 'b', 'c'])

chart_data
