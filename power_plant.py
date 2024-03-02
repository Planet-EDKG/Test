import requests
import json

url = "http://127.0.0.1:5000/receive_data"  

data_to_send = {
            "ID": "3",
            "name":"power_plant",
            "type":"producer",
            "amount":"1100"}

response = requests.post(url, json=data_to_send)