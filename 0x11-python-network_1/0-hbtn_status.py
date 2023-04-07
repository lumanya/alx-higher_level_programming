#!/usr/bin/python3
"""
0-hbtn_status- is the module that fetches https://alx-intranet.hbtn.io/status
bu use urllib package
"""


import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    html = html.decode('utf-8')

print("Body response:")
print("\t- type: {}".format(type(html)))
print("\t- content: {}".format(html))
print("\t- utf8 content: {}".format(html.encode('utf-8')))
