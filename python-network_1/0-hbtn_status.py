#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using urllib."""
import urllib.request


def fetch_status():
    """Fetch the status page and display the response body."""
    url = "https://intranet.hbtn.io/status"
    headers = {'cfclearance': 'true'}
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode('utf-8'))


if __name__ == "__main__":
    fetch_status()
