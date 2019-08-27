#!/usr/bin/python3
"""
use basic api 
"""

from sys import argv
from requests.auth import HTTPBasicAuth
import requests

if __name__ == "__main__":
    req = requests.get('https://api.github.com/user',
                        auth=HTTPBasicAuth(argv[1], argv[2]))
    json = resp.json()
    print(json.get('id'))
