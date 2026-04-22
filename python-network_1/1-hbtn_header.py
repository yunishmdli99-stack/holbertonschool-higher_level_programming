#!/usr/bin/python3
"""Sends a request to a URL and displays the X-Request-Id response header."""
import urllib.request
import sys


def get_request_id(url):
    """Fetch the given URL and print the value of X-Request-Id from headers."""
    with urllib.request.urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    get_request_id(sys.argv[1])
