from __future__ import print_function
import requests
import json
import pprint
pp = pprint.PrettyPrinter(indent=2)

API_KEY = "AIzaSyDqlY2dyOTrvcYWBtvsibdsetN14fJcnL4"


def get_data(address):
    r = 'https://www.googleapis.com/civicinfo/v2/elections?key=%s' % API_KEY
    response = requests.get(r)
    elections_data = json.loads(response.content)
    pp.pprint(elections_data)

    election_ids = [a['id'] for a in elections_data['elections']]

    elections = []
    for id_ in election_ids:
        params = {'address': address, 'electionId': id_}
        response = requests.get("https://www.googleapis.com/civicinfo/v2/voterinfo?key=%s" % API_KEY, params)
        content = json.loads(response.content)

        # Election data
        election = content['election']
        name = election['name']
        day = election['electionDay']
        division = election['ocdDivisionId']
        elections.append((name, day, division))
    return elections
