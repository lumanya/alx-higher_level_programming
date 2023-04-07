#!/usr/bin/python3
"""
Python Script that takes in a URl, sends a requets to the uRL and display the
body of th reponse
- if the HTTP status_code is greater that or equal to 400, print: Error code:
"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    with requests.get(url) as r:
        if r.status_code >= 400:
            print("Error code: {}".format(r.status_code))
        else:
            print(r.text)
