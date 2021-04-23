import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import dash_table


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
        html.Div([
            html.H1(children='Hello Dash'),

            html.Div(children='''
                Dash: A web application framework for Python.
            '''),

            dcc.Graph(
                id='graph1',
                figure=fig
            ),  
        ], className='six columns'),
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

     dcc.Dropdown(
    options=[
        {'label': '2020', 'value': 'NYC', 'disabled': True},
        {'label': '2021', 'value': 'MTL'},
        
    ],
)  ,
html.Br(),

       dcc.Slider(
    min=0,
    max=100,
    value=65,
    marks={
        0: {'label': '0 °C', 'style': {'color': '#77b0b1'}},
        26: {'label': '26 °C'},
        37: {'label': '37 °C'},
        100: {'label': '100 °C', 'style': {'color': '#f50'}}
    }
)  ,
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


    