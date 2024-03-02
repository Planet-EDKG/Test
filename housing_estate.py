import requests
import json

url = "http://127.0.0.1:5000/receive_data"  

data_to_send = {
            "ID": "2",
            "name":"housing_estate",
            "type":"consumer",
            "amount":"800"}
headers = {
    'Content-type':'application/json', 
    'Accept':'application/json'
}
data = {'key':'value'}
response = requests.post(url, json=data_to_send, headers=headers)
