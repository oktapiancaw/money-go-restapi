import requests

BASE = "http://127.0.0.1:5000/"

data = {
    "title" : "How to rich",
    "type" : "Wish",
    "description" : "test",
    "currency_target" : 100000000
}

response = requests.get(BASE)
print(response.json())