import requests
import json
import pprint


def getAccount(ID, tagline):
    response_api = requests.get(
        f'https://api.henrikdev.xyz/valorant/v1/account/{ID}/{tagline}')
    status = response_api.status_code
    data = response_api.text
    raw = json.loads(data)

    getAccount = {
        'puuid': [raw['data']['puuid']],
        'region': [raw['data']['region']],
        'accountlvl': [raw['data']['account_level']],
        'name': [raw['data']['name']],
        'tag': [raw['data']['tag']],
        'cardS': [raw['data']['card']['small']],
        'cardL': [raw['data']['card']['large']],
        'cardW': [raw['data']['card']['wide']],
        'cardID': [raw['data']['card']['id']],
    }

    pprint.pprint(getAccount)
    print(getAccount)


getAccount("Rampage", "2346")