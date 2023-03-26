import pandas as pd
import plotly.express as px
import streamlit as st

Data = pd.read_csv('https://raw.githubusercontent.com/nakhwaazizah/visdat/main/factbook.csv',index_col=0)

with st.sidebar:
      X = st.selectbox(
      'X',
      (Data.columns.values))
      Y = st.selectbox(
      'Y',
      (Data.columns.values))
      Size = st.selectbox(
      'Size',
      (Data.columns.values))
      Color = st.selectbox(
      'Color',
      (Data.columns.values))
      Circle_area = st.slider('Circle Area', 0, 100, 60)

      st.write('X:', X)
      st.write('Y:', Y)
      st.write('Size:', Size)
      st.write('Color:', Color)
      st.write("Circle Area:", Circle_area)

fig = px.scatter(data_frame=Data,x=X, y=Y,size =Size,color=Color,log_x=True,log_y=True,size_max=Circle_area)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)
