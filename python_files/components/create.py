import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash

class Create:
    def __init__(self):
        pass

    def create_function(self):
        self.create = html.Div([
            dbc.Row(dbc.Col(html.H1('Create User Account'), 
                width={'size':6, 'offset':4}), 
                style={'margin-bottom' : '50px',
                'margin-top' : '20px'},)

                , dcc.Location(id='create_user', refresh=True)

                ,dbc.Row(dbc.Col(html.P('Username'),width={'size':1 , 'offset':4}))

                , dbc.Row(dbc.Col(dbc.Input(id="username"
                    , type="text"
                    , placeholder="username"
                    , maxLength =15), 
                    width={'size':3 ,'offset':4 },
                    style={'margin-bottom' : '20px'}),)

                ,dbc.Row(dbc.Col(html.P('Password'),width={'size':1 , 'offset':4}))
                , dbc.Row(dbc.Col(dbc.Input(id="password"
                    , type="password"
                    , placeholder="password"), 
                    width={'size':3 ,'offset':4 },
                    style={'margin-bottom' : '20px'}),)

                ,dbc.Row(dbc.Col(html.P('Email'),width={'size':1 , 'offset':4}))
                , dbc.Row(dbc.Col(dbc.Input(id="email"
                    , type="email"
                    , placeholder="email"
                    , maxLength = 50),
                    width={'size':3, 'offset': 4},
                    style={'margin-bottom':'20px'}),)

                ,dbc.Row(dbc.Col(html.P('Age'),width={'size':1 , 'offset':4}))
                , dbc.Row(dbc.Col(dbc.Input(id="age", type="number", placeholder="age", min=1, max=100),
                width={'size':1 , 'offset':4},
                style={'margin-bottom':'20px'}),)

                ,dbc.Row([
                    dbc.Col(html.Div("Date"),width={"size":1, "offset": 4}),
                    dbc.Col(html.Div("Month"),width={"size":1}),
                    dbc.Col(html.Div("Year"),width={"size":1}),
                ],style={"margin-bottom":"10px"})

                ,dbc.Row([
                    dbc.Col(dbc.Input(id="date",type="number",placeholder="date",min=1,max=31),
                    width={'size':1,'offset':4},
                    style={'margin-bottom':'20px'}),

                    dbc.Col(dbc.Input(id="month",type="text",placeholder="month"),
                    width={'size':1},
                    style={'margin-bottom':'20px'}),

                    dbc.Col(dbc.Input(id="year",type="number",placeholder="year",min=1800,max=2021),
                    width={'size':1},
                    style={'margin-bottom':'20px'})],
                )

                , dbc.Row(dbc.Col(dbc.Button('Create User',color="primary", id='submit-val', n_clicks=0),
                width={'size':3,'offset':5},style={'margin-top':'20px','margin-bottom':'40px'}),)
                , html.Div(id='container-button-basic')
            ])#end div

        return self.create

