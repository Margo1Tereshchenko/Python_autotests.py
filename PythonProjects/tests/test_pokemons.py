import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2181cdb60ec99c127845a9e9e9e6a427'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '33493'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] =='Kotik'

@pytest.mark.parametrize('key, value', [('name', 'Kotik'), ('trainer_id', TRAINER_ID), ('id', '332836')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value