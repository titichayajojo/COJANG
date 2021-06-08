
import pandas as pd
import csv
import math
import json
year = 2021
month = 2
day = 9
df2 = pd.read_csv("codata.csv")
df2['cases'] = df2['cases'].fillna(0)
sp  =df2[(df2['year'] == year )]
sp  =sp[(sp['month'] == month )]
sp  =sp[(sp['day'] == day )]

state_id_map = {}
usa_states = json.load(open("others/usa5m.json",'r'))
for feature in usa_states['features']:
    feature['id'] = feature['properties']['STATE']
    state_id_map[feature['properties']['NAME']] = feature['id']
sp['id'] = sp['state'].apply(lambda x: state_id_map[x])
print(sp)
print(state_id_map)

# state_id_map = {}
# usa_states = json.load(open("others/usa5m.json",'r'))
# for feature in usa_states['features']:
#     feature['id'] = feature['properties']['STATE']
#     state_id_map[feature['properties']['NAME']] = feature['id']
# df2['id'] = df2['state'].apply(lambda x : state_id_map[x])
# print(df2.head(5))
# print(day,month,year)