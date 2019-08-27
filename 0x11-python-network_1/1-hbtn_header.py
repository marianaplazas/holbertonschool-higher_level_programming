#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL """


from sys import argv
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
