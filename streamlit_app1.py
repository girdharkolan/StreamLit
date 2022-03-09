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
    
    
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
    
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# st.columns lets you place widgets side-by-side, and st.expander lets you conserve space by hiding away large content.
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press meee!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting Hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

# progress bar
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
