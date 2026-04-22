#!/usr/bin/python3
"""Lists the 10 most recent commits of a GitHub repository."""
import requests
import sys


def list_commits(repo, owner):
    """Fetch and print the 10 most recent commits with sha and author."""
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    params = {'per_page': 10}
    headers = {'User-Agent': owner}
    r = requests.get(url, params=params, headers=headers)
    for commit in r.json():
        sha = commit.get('sha')
        name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, name))


if __name__ == "__main__":
    list_commits(sys.argv[1], sys.argv[2])
