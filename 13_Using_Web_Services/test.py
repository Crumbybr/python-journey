import urllib.request
import json

url = input('Enter url: ')
if len(url) < 1:
    url = "https://pokeapi.co/api/v2/pokemon/charizard"

url_open = urllib.request.urlopen(url) 
data = url_open.read().decode()

info = json.loads(data)

comments = info

print(comments)