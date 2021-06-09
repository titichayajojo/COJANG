import json
import urllib
import requests
import pandas
import pyrebase
import csv



class API:
    def __init__(self):
        print("eiei")
        self.states = []
        self.islands = [2, 12, 22, 26, 39, 43, 45, 53]
        
        self.url = 'https://api.apify.com/v2/datasets/FIbyK6uHUntt2kNy3/items?format=json&clean=1'

        self.headers = {'X-Parse-Application-Id': 'zoZ3zW1YABEWJMPInMwruD5XHgqT4QluDAAVx0Zz', # This is the fake app's application id
    'X-Parse-Master-Key': 'gIo7p0nTyt72aROJqf0ronfzxGKw8Unjw0Zk6qFm' # This is the fake app's readonly master key
}
        self.path = requests.get(self.url, headers=self.headers).content.decode('utf-8')
  
        self.csvfile = open('codata.csv','w', newline='')
        self.f = open('states_list.txt', 'r')
        self.obj = csv.writer(self.csvfile)

        self.states = self.f.read().split('\n')
        self.f.close()
        
        self.obj.writerow(('state', 'cases', 'year', 'month', 'day'))
        self.data = json.loads(self.path) # Here you have the data that you need


    def fetchData(self):
        state = None
        cases = None
        date = ''
        
        for i in self.data:
            if(i['casesByState'] != [] and len(i['casesByState']) == len(self.states)):
                if(date[:10] != i['lastUpdatedAtSource'][:10]):
                    for j in range(len(i['casesByState'])):
                        if j in self.islands:
                            continue
                        state = self.states[j]
                        cases = i['casesByState'][j]['casesReported']
                        date = i['lastUpdatedAtSource']
                        date = date[:10]
                        self.obj.writerow((state, cases, date[:4], date[5:7], date[8:19]))

        self.csvfile.close() 
        print("done")

