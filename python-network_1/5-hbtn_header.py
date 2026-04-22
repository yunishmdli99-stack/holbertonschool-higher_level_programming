#!/usr/bin/python3
"""Fetches a URL and prints the X-Request-Id response header value."""
import requests
import sys


def get_request_id(url):
    """Send a GET request and print the X-Request-Id header."""
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))


if __name__ == "__main__":
    get_request_id(sys.argv[1])
