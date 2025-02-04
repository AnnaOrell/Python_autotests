import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = ''
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "horohinyu@yandex.ru",
    "password": "Anna0502"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Стафф",
    "photo_id": 5
}
body_change = {
    "pokemon_id": "218114",
    "name": "Бочка"
}
body_to_catch = {
    "pokemon_id": "218114"
}

response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text) # регистрация тренера # подтверждение 

response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text) # подтверждение почты

response_create = requests.post(url= f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text) # создание покемона

response_change = requests.patch(url= f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text) # смена имени

response_to_catch = requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_to_catch)
print(response_to_catch.text) # поймать покемон в покебол