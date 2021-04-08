import urllib.request
import json
import time

while True:
    data=urllib.request.urlopen("https://api.thingspeak.com/channels/1349756/feeds.json?api_key=05QXJGNLQY3X9SPC&results=2")
    response=data.read()
    data=json.loads(response.decode())
    Entry=data['feeds']
    print("\n--------------------------------------------------------------\n")
    print("Previous Humidity : ",Entry[0]['field1'])
    print("Previous Temperature : ",Entry[0]['field2'])
    print("Humidity : ",Entry[1]['field1'])
    print("Temperature :",Entry[1]['field2'])
    print("\n--------------------------------------------------------------\n")
    time.sleep(10)
