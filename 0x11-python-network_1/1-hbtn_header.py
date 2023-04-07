#!/usr/bin/python3
"""
1-hbtn_header is the script that sends a request to URL and display the value
"""
import sys
import urllib.request


if __name__ == '__main__':
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        header = response.headers

    print(header['X-Request-Id'])
