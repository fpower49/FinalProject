import streamlit as st

import pandas as pd

import numpy as np

import pydeck as pdk



#creating a sample dataframe to plot

df = pd.DataFrame(np.random.randn(800, 2) / [50, 50] + [19.07, 72.87],columns=['latitude', 'longitude'])



#plotting the df

st.pydeck_chart(pdk.Deck(

     initial_view_state=pdk.ViewState(

         latitude=19.07,

         longitude=72.87,

         zoom=10,

         pitch=60,

     ),

     layers=[

         pdk.Layer(

            'HexagonLayer',

            data=df,

            get_position='[longitude, latitude]',

            radius=200,

            elevation_scale=4,

            elevation_range=[0, 1000],

            pickable=True,

            extruded=True,

         ),

         pdk.Layer(

             'ScatterplotLayer',

             data=df,

             get_position='[longitude, latitude]',

             get_radius=200,

         ),

     ],

 ))

