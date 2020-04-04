#!/usr/bin/python3
import numpy as np
import plotly.graph_objects as go
import pandas as pd
pid=pd.read_csv('./ping.csv')

trace1 = go.Scattergl(
    x=pid['time'],
    y=pid['ping'],
    mode='markers',
    marker=dict(
        opacity=0.8
    ),
)
layout = go.Layout(
    title='Time vs. Ping',
    xaxis=dict(
        title='Time'
    ),
    yaxis=dict(
        title='Ping (ms)'
    ),
    hovermode='closest',
    #showlegend=True
)

figure = go.Figure(data=trace1, layout=layout)
figure.show()
