#!/usr/bin/python3
"""Uses GitHub API with Basic Auth to display the user's id."""
import requests
import sys


def get_github_id(username, token):
    """Fetch GitHub user info and print the user id."""
    r = requests.get(
        "https://api.github.com/yunishmdli99-stack",
        auth=(username, token)
    )
    print(r.json().get('id'))


if __name__ == "__main__":
    get_github_id(sys.argv[1], sys.argv[2])
