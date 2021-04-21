import json
import urllib
import requests

url = 'https://parseapi.back4app.com/classes/Coronaviruscases_Covid19Case?count=1&limit=195&order=cases'
headers = {
    'X-Parse-Application-Id': '8bnYdl1uCG7ygDkHCknb1FBZABAyYtgs5dIwRVir', # This is your app's application id
    'X-Parse-REST-API-Key': 'LOFKb4T5SpYX9WlECGL20kzsNkCI8OkKhnlgPQwx' # This is your app's REST API key
}
data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
print(json.dumps(data, indent=2))

#for editing query data
#https://www.back4app.com/database/back4app/coronavirus-covid-19-api/get-started/python/rest-api/requests?appEntityId=ecd8bdeb-3394-4bee-9e48-67637bb85fc8
