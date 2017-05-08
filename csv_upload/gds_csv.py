import csv
import json
import http.client

conn = http.client.HTTPSConnection("test.server.com")
headers = {
    'authorization': "Bearer <basic_autherization_token>",
    'content-type': "application/json",
    }

def sendRequest(payload):
    conn.request("POST", "/api/1/users", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

with open('test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        oneEntry = json.dumps(row)
        sendRequest(oneEntry)
        # print(json.dumps(row, indent=2))
