import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import http.client
conn = http.client.HTTPSConnection("domain-name.com")
headers = {
    'authorization': "Bearer <BASIC_AUTHRIZATION_TOKEN>",
    'content-type': "application/json",
    }
def sendRequest(payload):
    conn.request("POST", "<END_POINT>", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

import csv
import json
with open('test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        oneEntry = json.dumps(row)
        sendRequest(oneEntry)
        # print(json.dumps(row, indent=2))
