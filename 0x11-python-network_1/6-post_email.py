#!/usr/bin/python3
"""
script that POST an email to server using requests
"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    with requests.post(url, data=data) as response:
        print(response.text)
