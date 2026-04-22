#!/usr/bin/python3
"""Sends a POST request to a URL with an email param and prints the body."""
import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """POST the given email to the URL and print the decoded response body."""
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    post_email(sys.argv[1], sys.argv[2])
