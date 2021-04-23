import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import dash_table


import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import json
import pandas as pd
import csv
import math
import plotly.express as px 


year = 2020
month = 5
day = 11
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




ALLOWED_TYPES = (
    "text", "number", "password", "email", "search",
    "tel", "url", "range", "hidden",
)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df_bar = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df_bar, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        # html.Div([
        #     html.H1(children='Hello Dash'),

        #     html.Div(children='''
        #         Dash: A web application framework for Python.
        #     '''),
        #      px.choropleth(df2,locations = 'id', geojson=usa_states,color='cases'),
           
        # ], className='six columns'),
        px.choropleth(df2,locations = 'id', geojson=usa_states,color='cases'),
        html.Div([
            html.H1(children='Hello Dash'),

            html.Div(children='''
                Dash: A web application framework for Python.
            '''),

            dcc.Graph(
                id='graph2',
                figure=fig
            ),  
        ], className='six columns'),
    ], className='row'),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children='Hello Dash'),
html.Br(),
        dcc.Input(id="dfalse", type="number", placeholder="year", min=2020, max=2021),
        dcc.Input(
            id="dtrue", type="text",
            debounce=True, placeholder="month",
        ),
        dcc.Input(
            id="input_range", type="text", placeholder="day",
            min=1, max=31, step=3,
        )
,
    ], className='row'),
    # ff.create_table(table_data, height_constant=60)

    html.Div([
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for Python.
        '''),
         dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

 ,
    ], className='row'),

    
])

if __name__ == '__main__':
    app.run_server(debug=True)


    