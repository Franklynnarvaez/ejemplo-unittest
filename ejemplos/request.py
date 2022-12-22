import requests


def checkResponseApi():
    r = requests.get('https://pokeapi.co/api/v2/pokemon/')
    return r.status_code


def getPokemonEncoding():
    r = requests.get('https://pokeapi.co/api/v2/pokemon/')
    return r.encoding


print(getPokemonEncoding())
