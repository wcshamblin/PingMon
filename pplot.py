#!/usr/bin/python3
import numpy as np
import plotly.graph_objects as go
import pandas as pd
pid=pd.read_csv('./ping.csv').sort_values('time')
np=pid[pid['ping'] == 0.0]
sp = go.Scattergl(
    x=pid['time'],
    y=pid['ping'],
    mode='markers',
    marker=dict(
        opacity=0.8),
    name="Host"
)
np = go.Scattergl(
    x=np['time'],
    y=np['ping'],
    mode='markers',
    marker=dict(
        opacity=0.8),
    name="No comm"
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
figure = go.Figure(data=[sp, np], layout=layout)
figure.show()
