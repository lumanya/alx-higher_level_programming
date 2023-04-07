#!/usr/bin/python3
"""
Python script takes in a letter and sends a POST request to
http://0.0.0.0/5000/search_user with letter as parameter
- the letter must be sent in the variable q
- if no argument is given, set q=""
"""
import sys
import requests

if __name__ == '__main__':
    url = 'http://cae7f21fb233.a3b94f4f.alx-cod.online:5000/search_user'
    if len(sys.argv) < 2:
        value = {"q": ""}
    else:
        value = {"q": sys.argv[1]}
    with requests.post(url, data=value) as r:
        json_data = r.json()

    if json_data:
        print("[{}] {}".format(json_data['id'], json_data['name']))
    else:
        print("No result")
