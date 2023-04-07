#!/usr/bin/python3
"""
Script that takes GitHUb creadentials (username and passowrd) as uses the
 GitHub API to display id
 Format first arguments is username, second password i.e token
"""
import sys
import requests

if __name__ == '__main__':
    username = sys.argv[1]
    token = sys.argv[2]

    # set up authentication
    auth = (username, token)
    url = "https://api.github.com/user"
    with requests.get(url, auth=auth) as r:
        print(r.json().get("id"))
