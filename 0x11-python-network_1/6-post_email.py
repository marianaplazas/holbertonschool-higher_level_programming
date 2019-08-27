#!/usr/bin/python3
"""
send post request
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}

    req = requests.post(url, data=payload)
    print(req.text)
