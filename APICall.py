import pprint
import json
import requests


# api call as function
def getAccount(ID, tagline):
    response_API = requests.get(f'https://api.henrikdev.xyz/valorant/v1/account/{ID}/{tagline}')
    status = response_API.status_code
    data = response_API.text
    raw = json.loads(data)

    puuid = raw['data']['puuid']
    region = raw['data']['region']
    accountlvl = raw['data']['account_level']
    name = raw['data']['name']
    tag = raw['data']['tag']
    cardS = raw['data']['card']['small']
    cardL = raw['data']['card']['large']
    cardW = raw['data']['card']['wide']
    cardID = raw['data']['card']['id']

    return puuid, region, accountlvl, name, tag, cardS, cardL, cardW, cardID


name = input("Enter your unique Riot ID.\n\t")
tag = input("Enter your Riot Tagline.\n\t")

ans = getAccount(name, tag)
print(ans)

