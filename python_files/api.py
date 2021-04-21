import json
import urllib
import requests
import pandas
import pyrebase
import csv

url = 'https://parseapi.back4app.com/classes/Covid19Case?count=1'
headers = {
    'X-Parse-Application-Id': 'zoZ3zW1YABEWJMPInMwruD5XHgqT4QluDAAVx0Zz', # This is the fake app's application id
    'X-Parse-Master-Key': 'gIo7p0nTyt72aROJqf0ronfzxGKw8Unjw0Zk6qFm' # This is the fake app's readonly master key
}
csvfile = open('codata.csv','w', newline='')
obj=csv.writer(csvfile)
obj.writerow(('countryName', 'cases', 'deaths', 'recovered'))
path = requests.get(url, headers=headers).content.decode('utf-8')
data = json.loads(path) # Here you have the data that you need
for k in data['results']:
    obj.writerow((k['countryName'], k['cases'], k['deaths'], k['recovered']))

csvfile.close()