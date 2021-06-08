
import dash 
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import json
import pandas as pd
import csv
import math
import plotly.express as px 
from plotly.subplots import make_subplots

import plotly.graph_objects as go

import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash_extensions.javascript import Namespace, arrow_function\
    
import dash_bootstrap_components as dbc
import plotly.figure_factory as ff

fips = ['06021', '06023', '06027',
        '06029', '06033', '06059',
        '06047', '06049', '06051',
        '06055', '06061']
values = range(len(fips))

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df = px.data.election()
geojson = px.data.election_geojson()
candidates = df.winner.unique()





colors = {
    'background': '#BBEEFC',
    'text': '#7FDBFF'
}
layout = html.Div(children =[

    dbc.Row(dbc.Col(html.H1("Cojung Web Application ", style={'text-align': 'center'}))),
    html.Div(id='output_container', children=[]),
    html.Br(),
    html.Br(),
    
    html.Div(children =[ 
         dbc.Row(dbc.Col(html.Div([html.P('Day', style={"height": "auto", "margin-bottom": "auto"}),
                      dcc.Input(id="In1", type="number", value='', ), ]),width={"offset":5},style={"margin-top":"20px"})),

         dbc.Row(dbc.Col(html.Div([html.P('Month', style={"height": "auto", "margin-bottom": "auto"}),
                      dcc.Input(id="In2", type="number", value='', ), ]) ,width={"offset":5},style={"margin-top":"20px"})),
         dbc.Row(dbc.Col(html.Div([html.P('Years', style={"height": "auto", "margin-bottom": "auto"}),
                      dcc.Input(id="In3", type="number", value='', ), ]),width={"offset":5},style={"margin-top":"20px"})),
         html.Br(), 
         dbc.Row(dbc.Col(dbc.Button('Submit', id='submit-val2', n_clicks=0,style={},color="primary",type="submit"),width={"offset":5})),
         
         dbc.Row(dbc.Col(html.Div(id='container-button-basic',
             children='Enter a value and press submit'),width={"offset":5},style={"margin-top":"20px"} ))
    ]),
     
    dcc.Graph(id="usa_map"),
    dcc.Graph(id="usa_bar"),
    
       
       
])

