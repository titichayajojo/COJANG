
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



year = 2021
month = 1
day = 1
df2 = pd.read_csv("codata.csv")
df2['cases'] = df2['cases'].fillna(0)
sp  =df2[(df2['year'] == year ) & (df2['month'] == month) & (df2['day'] == day)]
state_id_map = {}
usa_states = json.load(open("others/usa5m.json",'r'))
for feature in usa_states['features']:
    feature['id'] = feature['properties']['STATE']
    state_id_map[feature['properties']['NAME']] = feature['id']
df2['id'] = df2['state'].apply(lambda x : state_id_map[x])
print(df2.head(10))






import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ---------- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")
df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Other/Dash_Introduction/intro_bees.csv")

df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
print(df[:5])

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018}],
                 multi=False,
                 value=2015,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={}),
    html.Br(),
    dcc.Input(id="dfalse", type="number", placeholder="year", min=2020, max=2021),
        dcc.Input(
            id="dtrue", type="text",
            debounce=True, placeholder="month",
        ),
        dcc.Input(
            id="input_range", type="text", placeholder="day",
            min=1, max=31, step=3,
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



# #graph_twin
# @app.callback(
#     [Output(component_id='graph_twin', component_property='figure')],
#     [Input(component_id='slct_year', component_property='value')]
    
# )
# def update_graph_twin(option_slctd):
#     data_canada = px.data.gapminder().query("country == 'Canada'")
#     fig = px.bar(data_canada, x='year', y='pop')
#     return fig




# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Year"] == option_slctd]
    dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express
    # fig =  px.choropleth(df2,locations = 'id', geojson=usa_states,color='cases')
    # fig = make_subplots(rows=1 , cols=2)
    # fig.add_trace(
    #     go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
    #     row=1, col=1
    # )
    df3 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')
    fig = go.Figure(data=go.Choropleth(
    locations=df3['code'], # Spatial coordinates
    z = df3['total exports'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Millions USD",
))
   
    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)

    
# https://youtu.be/hSPmj7mK6ng 