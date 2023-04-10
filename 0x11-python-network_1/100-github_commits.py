#!/usr/bin/python3
""" python script that  prints respo name  and commit
Requiremts
- first arguments will be the repository name
- the second argumets will be the owner name
- you must use the package requests and ys
"""
import sys
import requests


if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo_name)
    with requests.get(url) as r:
        if r.status_code == 200:
            commits = r.json()
            for commit in commits[:10]:
                sha = commit.get('sha')
                author_name = commit.get('commit').get('author').get('name')
                print(f"{sha}: {author_name}")
