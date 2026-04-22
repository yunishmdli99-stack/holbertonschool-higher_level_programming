#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using the requests package."""
import requests


def fetch_status():
    """Fetch the status page and display the response body details."""
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(r.text))
    print("\t- content:", r.text)


if __name__ == "__main__":
    fetch_status()
