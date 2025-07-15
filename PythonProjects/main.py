import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2181cdb60ec99c127845a9e9e9e6a427'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Kotik",
    "photo_id": "-1"
}

body_alter = {
    "pokemon_id": "332859",
    "name": "Krolik",
    "photo_id": "-1"
}

body_grasp = {
    "pokemon_id": "332836"
    }

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
pokemon_id = response_create.json()['id']
print(pokemon_id)

response_alter = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_alter)
print(response_alter.json)

response_grasp = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_grasp)
print(response_grasp.json)