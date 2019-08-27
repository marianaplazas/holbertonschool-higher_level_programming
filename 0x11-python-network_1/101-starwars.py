#!/usr/bin/python3
"""
Star wars 1.0
"""
import requests
import sys

if __name__ == "__main__":
    search = sys.argv[1]
    url = "https://swapi.co/api/people/?search=" + search
    req = requests.get(url)
    data = dict(req.json())
    print("Number of result: {}".format(data.get("count")))

    while req.json()['next'] is not None:
        for r in data.get("results"):
            print(r.get("name"))
        req = requests.get(req.json()['next'])
        data = dict(req.json())

    for r in data.get("results"):
        print(r.get("name"))
