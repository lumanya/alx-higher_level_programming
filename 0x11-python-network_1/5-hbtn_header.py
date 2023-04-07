#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the values
of the variable X-Request-Id header using requests module\
"""

import sys
import requests

if __name__ == '__main__':
    with requests.get(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])
