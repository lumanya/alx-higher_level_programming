#!/usr/bin/python3
"""
Script that takes GitHUb creadentials (username and passowrd) as uses the
 GitHub API to display id
 Format first arguments is username, second password i.e token
"""
import sys
import requests

if __name__ == '__main__':
    headers = {"Authorization": "Bearer" + sys.argv[2]}
    url = "https://api.github.com/users/{}".format(sys.argv[1])
    with requests.get(url, headers=headers) as r:
        json_data = r.json()
    print(json_data['id'])
