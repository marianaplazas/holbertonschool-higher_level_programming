#!/usr/bin/python3
"""
fetch 
"""
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    print("Body response:")
    print("\t- type: {}".format(type(requests.get(url).text)))
    print("\t- content: {}".format(requests.get(url).text))
