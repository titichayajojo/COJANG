import json
import urllib
import requests

url = 'https://parseapi.back4app.com/classes/Covid19Case?count=1'
headers = {
    'X-Parse-Application-Id': 'zoZ3zW1YABEWJMPInMwruD5XHgqT4QluDAAVx0Zz', # This is the fake app's application id
    'X-Parse-Master-Key': 'gIo7p0nTyt72aROJqf0ronfzxGKw8Unjw0Zk6qFm' # This is the fake app's readonly master key
}
data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
print(json.dumps(data, indent=2))