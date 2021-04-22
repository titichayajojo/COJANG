import json
import urllib
import requests
import pandas
import pyrebase
import csv

url = 'https://api.apify.com/v2/datasets/FIbyK6uHUntt2kNy3/items?format=json&clean=1'
headers = {
    'X-Parse-Application-Id': 'zoZ3zW1YABEWJMPInMwruD5XHgqT4QluDAAVx0Zz', # This is the fake app's application id
    'X-Parse-Master-Key': 'gIo7p0nTyt72aROJqf0ronfzxGKw8Unjw0Zk6qFm' # This is the fake app's readonly master key
}
csvfile = open('codata.csv','w', newline='')
obj = csv.writer(csvfile)
obj.writerow(('state', 'cases', 'date'))
path = requests.get(url, headers=headers).content.decode('utf-8')
data = json.loads(path) # Here you have the data that you need
state = None
cases = None
date = None
for i in data:
    for j in range(len(i['casesByState'])):
        print(j)
        state = i['casesByState'][j]['name']
        cases = i['casesByState'][j]['casesReported']
        date = i['lastUpdatedAtSource']
        obj.writerow((state, cases, date))

csvfile.close()