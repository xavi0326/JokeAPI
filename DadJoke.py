import requests
from pprint import pprint
import json


url = "https://icanhazdadjoke.com/"

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

responseJson = response.json()


pprint(responseJson)