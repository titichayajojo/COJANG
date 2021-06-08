
import dash 
import dash_core_components as dcc
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
layout = html.Div(style={'backgroundColor': colors['background']},children =[

    html.H1("Cojung Web Application ", style={'text-align': 'center'}),
    html.Div(id='output_container', children=[]),
    html.Br(),
    html.Br(),
    html.Div(children =[ 
         html.Div([html.P('Day', style={"height": "auto", "margin-bottom": "auto"}),
                      dcc.Input(id="In1", type="number", value='', ), ]),
         html.Div([html.P('Month', style={"height": "auto", "margin-bottom": "auto"}),
                      dcc.Input(id="In2", type="number", value='', ), ]),
         html.Div([html.P('Years', style={"height": "auto", "margin-bottom": "auto"}),
                      dcc.Input(id="In3", type="number", value='', ), ]),
         html.Br(), 
         html.Button('Submit', id='submit-val2', n_clicks=0,style={}),
         html.Div(id='container-button-basic',
             children='Enter a value and press submit')
    ]),
     dcc.Graph(id="usa_map"),
     dcc.RadioItems(
        id='candidate', 
        options=[{'value': x, 'label': x} 
                 for x in candidates],
        value=candidates[0],
        labelStyle={'display': 'inline-block'}
    ),

    
       
         html.Div([
        html.Div([
            html.H3('Column 1'),
            dcc.Graph(id="usa_bar"),
        ], className="six columns"),

        html.Div([  
            html.H3('Column 2'),
            dcc.Graph(id='g2', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="six columns"),
    ], className="row")
])

