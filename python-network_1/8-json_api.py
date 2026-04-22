#!/usr/bin/python3
"""Sends a POST request with a letter and displays the search result."""
import requests
import sys


def search_user(q):
    """POST q to the search endpoint and print result or error message."""
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        data = r.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(q)
