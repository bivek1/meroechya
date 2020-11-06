import urllib.request
import json

with urllib.request.urlopen("https://geolocation-db.com/json") as url:
    data = json.loads(url.read().decode())
    print(data)

