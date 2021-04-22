import json
import pandas as pd

usa_states = json.load(open("others/united_state.json",'r'))
print(usa_states['features'][1])
df = pd.read_csv("codata.csv")
df['Cases'] = df['cases']
print(df['Cases'])
state_id_map = {}
for feature in usa_states['features']:
    feature['uni_id'] = feature['properties']['STATE']
    state_id_map[feature['properties']['NAME']] = feature['uni_id']
print(state_id_map)
df['uni_id'] = df['state'].apply(lambda x: state_id_map[x] if state_id_map[x] else )






print(df['uni_id'])
