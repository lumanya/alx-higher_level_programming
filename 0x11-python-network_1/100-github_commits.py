#!/usr/bin/python3

import sys
import requests


if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo_name)
    print(url)
    with requests.get(url) as r:
        if r.status_code == 200:
            commits = r.json()
            for commit in commits[:10]:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
