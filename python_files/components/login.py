import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash

class Login:
    def __init__(self):
        pass

    def login_function(self):
        self.login =  html.Div([dcc.Location(id='url_login', refresh=True)
            , dbc.Row(dbc.Col(html.H1('''Please log in to continue''', id='h1'),width={"offset":4},style={"margin-top":"20px","margin-bottom":"50px"}))
            , dbc.Row(dbc.Col(dbc.Input(placeholder='username',
                    type='text',
                    id='uname-box'),width={"offset":5},style={"margin-bottom":"20px"}))
            , dbc.Row(dbc.Col(dbc.Input(placeholder='password',
                    type='password',
                    id='pwd-box'),width={"offset":5},style={"margin-bottom":"20px"}))
            , dbc.Row(dbc.Col(dbc.Button(children='Login',
                    color="primary",
                    n_clicks=0,
                    type='submit',
                    id='login-button'),width={"offset":5}))
            , html.Div(children='', id='output-state')
            
        ]) #end div
        return self.login

    def failed_function(self):
        self.failed = html.Div([ dcc.Location(id='url_login_df', refresh=True)
                    , html.Div([dbc.Row(dbc.Col(html.H2('Log in Failed. Please try again'),width={"offset":5},style={"margin-top":"20px","margin-bottom" :"50px"}))
                            , html.Br()
                            , html.Div([self.login])
                            , html.Br()
                            , dbc.Row(dbc.Col(dbc.Button(id='back-button',color="primary", children='Go back', n_clicks=0),width={"offset":5},style={"margin-bottom":"20px"}))
                        ]) #end div
                ]) #end div
        return self.failed
    
    def logout_function(self):
        self.logout = html.Div([dcc.Location(id='logout', refresh=True)
            , html.Br()
            , html.Div(html.H2('You have been logged out - Please login'))
            , html.Br()
            , html.Div([self.login])
            , html.Button(id='back-button', children='Go back', n_clicks=0)
        ])#end div

        return self.logout
