
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import json
import pandas as pd
import csv


year = 2021
df = pd.read_csv("codata.csv")

df2 = df[df['date'].map(lambda x:  int(x.split('-')[0]) == 2020 )]

choosing_date = {}

df3 = df[df['date'].map(lambda x: x== "2020-03-13")]
print(len(df3))
print(df3['state'].unique())
print(df3['state'].nunique())

