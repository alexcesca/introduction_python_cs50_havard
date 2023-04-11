import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=506&term="+sys.argv[1])

obj = json.loads(json.dumps(response.json(), indent=2))

for result in obj['results']:
   print(result["trackName"])
