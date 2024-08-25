from pprint import pprint
import requests
APIKEY = 'f9e2197401bc922024ce6d7723074eb3'
location = 'Cape coast'
r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={APIKEY}')

if r.status_code == 200:
    pprint(r.json())
else:
    print('how are you?')