import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State
from sqlalchemy import Table, create_engine
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import warnings
import os
from flask_login import login_user, logout_user, current_user, LoginManager, UserMixin
import configparser
import pandas as pd

import python_files.test1_boon as activity
import json
import plotly.express as px
import python_files.api as ap

import python_files.components.create as create_component
import python_files.components.login as login_component
import python_files.components.success as success_component

warnings.filterwarnings("ignore")
conn = sqlite3.connect('data.sqlite')
engine = create_engine('sqlite:///data.sqlite')
db = SQLAlchemy()

config = configparser.ConfigParser()
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server = app.server
app.config.suppress_callback_exceptions = True

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable = False)
    password = db.Column(db.String(80))
    email = db.Column(db.String(50), unique=True)
    age = db.Column(db.Integer)
    date = db.Column(db.Integer)
    month = db.Column(db.String(20))
    year = db.Column(db.Integer)
    
Users_tbl = Table('users', Users.metadata)

#fuction to create table using Users class
def create_users_table():
    Users.metadata.create_all(engine)


class Users(UserMixin, Users):
    pass


# config
server.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI='sqlite:///data.sqlite',
    SQLALCHEMY_TRACK_MODIFICATIONS=False)

db.init_app(server)
# Setup the LoginManager for the server
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/login'
#User as base
# Create User class with UserMixin


Create = create_component.Create()
Login = login_component.Login()
Success = success_component.Success()


create = Create.create_function()
login = Login.login_function()
success = Success.success_function()
failed = Login.failed_function()
logout = Login.login_function()



app.layout= html.Div([
            html.Div(id='page-content', className='content')
            ,  dcc.Location(id='url', refresh=False)
        ])

# callback to reload the user object
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))
@app.callback(
    Output('page-content', 'children')
    , [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return create
    elif pathname == '/login':
        return login
    elif pathname == '/success':
        if current_user.is_authenticated:
            return success
        else:
            return failed
    elif pathname =='/data':
        if current_user.is_authenticated:
            return activity.layout
    elif pathname == '/logout':
        if current_user.is_authenticated:
            logout_user()
            return logout
        else:
            return logout
    else:
        return '404'

#set the callback for the dropdown interactivity

@app.callback(
   [Output('container-button-basic', "children")]
    , [Input('submit-val', 'n_clicks')]
    , [State('username', 'value'), State('password', 'value'), State('email', 'value'), State('age', 'value'), State('date', 'value'), State('month', 'value'), State('year', 'value')])
def insert_users(n_clicks, un, pw, em, ag, dt, mn, yr):
    hashed_password = generate_password_hash(pw, method='sha256')
    if un is not None and pw is not None and em is not None:
        ins = Users_tbl.insert().values(username=un,  password=hashed_password, email=em, age=ag, date=dt, month=mn, year=yr)
        conn = engine.connect()
        conn.execute(ins)
        conn.close()
        return [login]
    else:
        return [dbc.Row(dbc.Col(html.Div([html.H5('Already have a user account?'), dcc.Link('Click here to Log In', href='/login')]),width={"offset":4}))]
@app.callback(
    Output('url_login', 'pathname')
    , [Input('login-button', 'n_clicks')]
    , [State('uname-box', 'value'), State('pwd-box', 'value')])
def successful(n_clicks, input1, input2):
    user = Users.query.filter_by(username=input1).first()
    if user:
        if check_password_hash(user.password, input2):
            login_user(user)
            return '/success'
        else:
            pass
    else:
        pass

@app.callback(
    Output('output-state', 'children')
    , [Input('login-button', 'n_clicks')]
    , [State('uname-box', 'value'), State('pwd-box', 'value')])
def update_output(n_clicks, input1, input2):
    if n_clicks > 0:
        user = Users.query.filter_by(username=input1).first()

        if user:
            if check_password_hash(user.password, input2):
                return ''
            else:
                return [dbc.Row(dbc.Col(html.Div([html.H5('Want to register ?'), 
                dcc.Link('Click here to register', href='/')]),width={"offset":4},style={"margin-top":"50px"})),
                dbc.Row(dbc.Col(html.Div(html.P('Incorect username or password')),className="text-warning",width={"offset":5},style={"margin-top":"20px"}))]
        else:
            return [dbc.Row(dbc.Col(html.Div([html.H5('Want to register ?'), 
                dcc.Link('Click here to register', href='/')]),width={"offset":4},style={"margin-top":"50px"})),
                dbc.Row(dbc.Col(html.Div(html.P('Incorect username or password')),className="text-warning",width={"offset":5},style={"margin-top":"20px"}))]
    else:
        return [dbc.Row(dbc.Col(html.Div([html.H5('Want to register ?'), dcc.Link('Click here to register', href='/')]),width={"offset":4},style={"margin-top":"50px"}))]
    
    

@app.callback(
    Output('url_login_success', 'pathname')
    , [Input('back-button', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/'

@app.callback(
    Output('url_login_df', 'pathname')
    , [Input('back-button', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/'

# Create callbacks
@app.callback(
    Output('url_logout', 'pathname')
    , [Input('back-button', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/'

@app.callback(
    [dash.dependencies.Output('usa_map', component_property='figure'),
    dash.dependencies.Output('usa_bar', component_property='figure')
    ],
    [dash.dependencies.Input('submit-val2', 'n_clicks')],
    [dash.dependencies.State('In1', 'value'),
    dash.dependencies.State('In2', 'value'),
    dash.dependencies.State('In3', 'value')])
    
def update_output(click,in1,in2,in3):
    year = in3
    month = in2
    day = in1
    df2 = pd.read_csv("codata.csv")
    df2['cases'] = df2['cases'].fillna(0)
    sp  =df2[(df2['year'] == year )]
    sp  =sp[(sp['month'] == month )]
    sp  =sp[(sp['day'] == day )]
    print(sp.head(5))
    state_id_map = {}
    usa_states = json.load(open("others/usa5m.json",'r'))
    for feature in usa_states['features']:
        feature['id'] = feature['properties']['STATE']
        state_id_map[feature['properties']['NAME']] = feature['id']
    sp['id'] = sp['state'].apply(lambda x: state_id_map[x])
    fig = px.choropleth(sp,locations='id',geojson=usa_states,color='cases',scope="usa")
    fig2 = px.bar(sp,x="state",y="cases")
    fig2.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig2.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    return fig,fig2




if __name__ == '__main__':
    #Fetching data from 
    # dataAPI = ap.API()
    # dataAPI.fetchData()
    c = conn.cursor()
    df = pd.read_sql('select * from users', conn)
    print(df)
    app.run_server(debug=True)
   