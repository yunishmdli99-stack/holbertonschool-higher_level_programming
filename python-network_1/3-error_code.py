#!/usr/bin/python3
"""Fetches a URL and prints the response body, or an HTTP error code."""
import urllib.request
import urllib.error
import sys


def fetch_url(url):
    """Send a GET request and print body or HTTP error code."""
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    fetch_url(sys.argv[1])
