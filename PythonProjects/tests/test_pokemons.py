import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = ''
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = "21747"

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200 # GET /trainers
def test_response_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Ананасик' # ответ с именем твоего тренера
