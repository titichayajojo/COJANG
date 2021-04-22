import json
import urllib
import requests
import pandas
import pyrebase
import csv

states = []
url = 'https://api.apify.com/v2/datasets/FIbyK6uHUntt2kNy3/items?format=json&clean=1'
headers = {
    'X-Parse-Application-Id': 'zoZ3zW1YABEWJMPInMwruD5XHgqT4QluDAAVx0Zz', # This is the fake app's application id
    'X-Parse-Master-Key': 'gIo7p0nTyt72aROJqf0ronfzxGKw8Unjw0Zk6qFm' # This is the fake app's readonly master key
}
csvfile = open('codata.csv','w', newline='')
f = open('states_list.txt', 'r')

states = f.read().split('\n')
f.close()

obj = csv.writer(csvfile)
obj.writerow(('state', 'cases', 'date'))
path = requests.get(url, headers=headers).content.decode('utf-8')
data = json.loads(path) # Here you have the data that you need

state = None
cases = None
date = None

for i in data:
    if(i['casesByState'] != [] and len(i['casesByState']) == len(states)):
        for j in range(len(i['casesByState'])):
            state = states[j]
            cases = i['casesByState'][j]['casesReported']
            date = i['lastUpdatedAtSource']
            obj.writerow((state, cases, date[:10]))

csvfile.close() 
print("done")