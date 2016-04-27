from __future__ import print_function
import requests
import json
import pprint
pp = pprint.PrettyPrinter(indent=2)

API_KEY = "AIzaSyDqlY2dyOTrvcYWBtvsibdsetN14fJcnL4"

# Send first query for elections
r = 'https://www.googleapis.com/civicinfo/v2/elections?key=%s' % API_KEY
response = requests.get(r)

elections_data = json.loads(response.content)
pp.pprint(elections_data)


election_ids = [a['id'] for a in elections_data['elections']]
pp.pprint(election_ids)

# Loop through election ids and get voter data for one address
