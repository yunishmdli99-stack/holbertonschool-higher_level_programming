#!/usr/bin/python3
"""Sends a POST request with an email parameter and prints the response."""
import requests
import sys


def post_email(url, email):
    """POST email to the URL and print the response body."""
    r = requests.post(url, data={'email': email})
    print(r.text)


if __name__ == "__main__":
    post_email(sys.argv[1], sys.argv[2])
