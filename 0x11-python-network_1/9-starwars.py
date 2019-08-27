#!/usr/bin/python3
"""
May the force be with you
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://swapi.co/api/people'
    letter = {'search': argv[1]}
    req = requests.get(url, params=letter)

    response = req.json()
    print("Number of results: {}".format(response.get('count')))
    for n in response.get('results'):
        print(n.get('name'))
