import requests

heroes_url = "https://superheroapi.com/api/2619421814940190/search/"
superheroes = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]

for heroe in superheroes:
    res = requests.get(heroes_url + heroe['name'])
    heroe['intelligence'] = int(res.json()['results'][0]['powerstats']['intelligence'])

print(sorted(superheroes, key=lambda heroe: -heroe['intelligence'])[0]['name'])