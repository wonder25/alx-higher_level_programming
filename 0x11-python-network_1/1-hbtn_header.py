#!/usr/bin/python3
"""takes url, sends a request to the url and displays the value of request-id"""

from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.getheader("X-Request-Id")
        print(f"{html}")
