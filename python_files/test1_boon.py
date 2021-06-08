
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


df = px.data.election()
geojson = px.data.election_geojson()
candidates = df.winner.unique()




app = dash.Dash(__name__)



colors = {
    'background': '#BBEEFC',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']},children =[

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),
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
         html.Button('Submit', id='submit-val', n_clicks=0,style={}),
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
            dcc.Graph(id='g1', figure={})
        ], className="six columns"),

        html.Div([  
            html.H3('Column 2'),
            dcc.Graph(id='g2', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="six columns"),
    ], className="row")
])



@app.callback(
    dash.dependencies.Output('usa_map', component_property='figure'),
    [dash.dependencies.Input('submit-val', 'n_clicks')],
    [dash.dependencies.State('In1', 'value'),
    dash.dependencies.State('In2', 'value'),
    dash.dependencies.State('In3', 'value')])
    
def update_output(click,in1,in2,in3):
    print(in1)
    year = in3
    month = in2
    day = in1
    df2 = pd.read_csv("codata.csv")
    df2['cases'] = df2['cases'].fillna(0)
    sp  =df2[(df2['year'] == year ) & (df2['month'] == month) & (df2['day'] == day)]
    state_id_map = {}
    usa_states = json.load(open("others/usa5m.json",'r'))
    for feature in usa_states['features']:
        feature['id'] = feature['properties']['STATE']
        state_id_map[feature['properties']['NAME']] = feature['id']
    df2['id'] = df2['state'].apply(lambda x : state_id_map[x])
    print(df2.head(5))
    print(day,month,year)
    fig = px.choropleth(locations=["CA", "TX", "NY"], locationmode="USA-states", color=[1,2,3], scope="usa")
    return fig 







# @app.callback(
#      dash.dependencies.Output('us_map', 'children'),
#      [dash.dependencies.Input('submit-val', 'n_clicks')],
    

# def map(click):
#     print(in1)
#     return ' {}/{}/{} '.format(
#         in1,
#         in2,
#         in3)
    

if __name__ == '__main__':
    app.run_server(debug=True)

