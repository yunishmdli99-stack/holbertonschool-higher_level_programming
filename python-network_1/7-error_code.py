#!/usr/bin/python3
"""Fetches a URL and prints the body or an error code if status >= 400."""
import requests
import sys


def fetch_url(url):
    """Send a GET request and print body or HTTP error code."""
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        print(r.text)


if __name__ == "__main__":
    fetch_url(sys.argv[1])
