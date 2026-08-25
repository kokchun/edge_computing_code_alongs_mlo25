import json 
import network
import rp2
import time

rp2.country("SE")

with open("wifi_credentials.json") as file:
    credentials = json.load(file)

print(credentials)
