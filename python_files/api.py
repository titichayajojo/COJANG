import json
import urllib
import requests
import pandas
import pyrebase
import csv

states = []
islands = [2, 12, 22, 26, 39, 43, 45, 53]
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
obj.writerow(('state', 'cases', 'year', 'month', 'day'))
path = requests.get(url, headers=headers).content.decode('utf-8')
data = json.loads(path) # Here you have the data that you need

state = None
cases = None
date = ''

for i in data:
    if(i['casesByState'] != [] and len(i['casesByState']) == len(states)):
        if(date[:10] != i['lastUpdatedAtSource'][:10]):
            for j in range(len(i['casesByState'])):
                if j in islands:
                    continue
                state = states[j]
                cases = i['casesByState'][j]['casesReported']
                date = i['lastUpdatedAtSource']
                date = date[:10]
                obj.writerow((state, cases, date[:4], date[5:7], date[8:19]))

csvfile.close() 
print("done")