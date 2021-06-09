import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash

class Success:
    def __init__(self):
        pass

    def success_function(self):
        self.success = html.Div([dcc.Location(id='url_login_success', refresh=True)
                    , html.Div([dbc.Row(dbc.Col(html.H2('WELCOME!'),width={"offset":5},style={"margin-top":"20px","margin-bottom" :"50px"}))
                            , html.Br()
                            , dbc.Row(dbc.Col(html.P(["The COVID-19 pandemic, also known as the coronavirus pandemic, is an ongoing global pandemic of coronavirus disease 2019 (COVID-19)", html.Br(), "caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The virus was first identified in December 2019 in Wuhan, China.", html.Br(), " The World Health Organization declared a Public Health Emergency of International Concern regarding COVID-19 on 30 January 2020,", html.Br(), " and later declared a pandemic on 11 March 2020.As of 8 June 2021, more than 173 million cases have been confirmed, with more than 3.73 million", html.Br(), " confirmed deaths attributed to COVID-19, making it one of the deadliest pandemics in history. symptoms of COVID-19 are highly variable,", html.Br(), " ranging from none to life-threateningly severe. COVID-19 transmits when people breathe in air contaminated by droplets and small airborne particles.", html.Br(), " The risk of breathing these in is highest when people are in close proximity, but they can be inhaled over longer distances, particularly indoors.", html.Br(), " Transmission can also occur if splashed or sprayed with contaminated fluids, in the eyes, nose or mouth, and, rarely, via contaminated surfaces.", html.Br(), " People remain contagious for up to 20 days, and can spread the virus even if they do not develop any symptoms."]),width={"offset":3},style={"margin-right":"20px"}))
                            
                        ]) #end div
                        ,dbc.Row(dbc.Col(dbc.Card(
                    [
                dbc.CardImg(src="/assets/Corona-19virus.jpg", top=True),
                dbc.CardBody(
                    [
                        html.H4("Cojung Map", className="card-title"),
                        html.P(
                            "Covid-19 in the United States of America"
                            "Dash Board from 13-03-2020 to current date (Last Update).",
                            className="card-text",
                        ),
                        dcc.Link('DashBoard', href = '/data'),
                    ]
                ),
            ],
            style={"width": "18rem"},
        ),width={"offset":5},style={"margin-bottom":"20px"}))
                    , html.Div([html.Br()
                            , dbc.Row(dbc.Col(dbc.Button(id='back-button',color="primary", children='Go back', n_clicks=0),width={"offset":5},style={"margin-bottom":"20px"}))
                        ]) #end div
                ]) #end div
        return self.success