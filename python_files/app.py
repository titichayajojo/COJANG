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

warnings.filterwarnings("ignore")
conn = sqlite3.connect('data.sqlite')
engine = create_engine('sqlite:///data.sqlite')
db = SQLAlchemy()
config = configparser.ConfigParser()
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable = False)
    email = db.Column(db.String(50), unique=True)
    age = db.Column(db.Integer, nullable = False)
    date = db.Column(db.Integer,nullable = False)
    month = db.Column(db.String(30),nullable = False)
    year = db.Column(db.Integer,nullable = False)
    password = db.Column(db.String(80))
Users_tbl = Table('users', Users.metadata)

#fuction to create table using Users class
def create_users_table():
    Users.metadata.create_all(engine)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server = app.server
app.config.suppress_callback_exceptions = True

# config
server.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI='sqlite:///data.sqlite',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
db.init_app(server)
# Setup the LoginManager for the server
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/login'
#User as base
# Create User class with UserMixin
class Users(UserMixin, Users):
    pass
create = html.Div([
    dbc.Row(dbc.Col(html.H1('Create User Account'), 
        width={'size':6, 'offset':4}), 
        style={'margin-bottom' : '50px',
        'margin-top' : '20px'},)
        , dcc.Location(id='create_user', refresh=True)
        ,html.P('username', style={'margin-left':650})
        , dbc.Row(dbc.Col(dbc.Input(id="username"
            , type="text"
            , placeholder="Enter your username"
            , maxLength =15), 
            width={'size':3 ,'offset':4 },
            style={'margin-bottom' : '20px'}),)

        , dbc.Row(dbc.Col(dbc.Input(id="password"
            , type="password"
            , placeholder="password"), 
            width={'size':3 ,'offset':4 }),)

        , dbc.Row(dbc.Col(dbc.Input(id="email"
            , type="email"
            , placeholder="email"
            , maxLength = 50),
            width={'size':3, 'offset': 4},
            style={'margin-top':'20px'}),)

        , dbc.Row(dbc.Col(dbc.Input(id="age", type="number", placeholder="age", min=1, max=100),
        width={'size':1 , 'offset':4},
        style={'margin-top':'20px'}),)

        ,dbc.Row([
            dbc.Col(dbc.Input(id="date",type="number",placeholder="date",min=1,max=31),
            width={'size':1,'offset':4},
            style={'margin-top':'20px'}),

            dbc.Col(dbc.Input(id="month",type="text",placeholder="month"),
            width={'size':1},
            style={'margin-top':'20px'}),

            dbc.Col(dbc.Input(id="year",type="number",placeholder="year",min=1800,max=2021),
            width={'size':1},
            style={'margin-top':'20px'})],
        )

        , dbc.Row(dbc.Col(dbc.Button('Create User',color="primary", id='submit-val', n_clicks=0),
        width={'size':3,'offset':5},style={'margin-top':'20px','margin-top':'40px'}),)
        , html.Div(id='container-button-basic')
    ])#end div


login =  html.Div([dcc.Location(id='url_login', refresh=True)
            , html.H2('''Please log in to continue:''', id='h1')
            , dcc.Input(placeholder='Enter your username',
                    type='text',
                    id='uname-box')
            , dcc.Input(placeholder='Enter your password',
                    type='password',
                    id='pwd-box')
            , html.Button(children='Login',
                    n_clicks=0,
                    type='submit',
                    id='login-button')
            , html.Div(children='', id='output-state')
        ]) #end div
success = html.Div([dcc.Location(id='url_login_success', refresh=True)
            , html.Div([html.H2('Login successful.')
                    , html.Br()
                    , html.P('Select a Dataset')
                    , dcc.Link('Data', href = '/data')
                ]) #end div
            , html.Div([html.Br()
                    , html.Button(id='back-button', children='Go back', n_clicks=0)
                ]) #end div
        ]) #end div


failed = html.Div([ dcc.Location(id='url_login_df', refresh=True)
            , html.Div([html.H2('Log in Failed. Please try again.')
                    , html.Br()
                    , html.Div([login])
                    , html.Br()
                    , html.Button(id='back-button', children='Go back', n_clicks=0)
                ]) #end div
        ]) #end div
logout = html.Div([dcc.Location(id='logout', refresh=True)
        , html.Br()
        , html.Div(html.H2('You have been logged out - Please login'))
        , html.Br()
        , html.Div([login])
        , html.Button(id='back-button', children='Go back', n_clicks=0)
    ])#end div
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
            pass
            #return
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
    , [State('username', 'value'), State('password', 'value'), State('email', 'value'), State('age','value'), State('date','value'), State('month','value'), State('year','value')])
def insert_users(n_clicks, un, pw, em, ag, dt, mn, yr):
    hashed_password = generate_password_hash(pw, method='sha256')
    if un is not None and pw is not None and em is not None and ag is not None:
        ins = Users_tbl.insert().values(username=un,  password=hashed_password, email=em, age=ag, date=dt, month=mn, year=yr)
        conn = engine.connect()
        conn.execute(ins)
        conn.close()
        return [login]
    else:
        return [html.Div([html.H2('Already have a user account?'), dcc.Link('Click here to Log In', href='/login')])]
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
                return 'Incorrect username or password'
        else:
            return 'Incorrect username or password'
    else:
        return ''
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


if __name__ == '__main__':
    #create the table
    #create_users_table()
    
    
    c = conn.cursor()
    df = pd.read_sql('select * from users', conn)
    print(df)
    app.run_server(debug=True)