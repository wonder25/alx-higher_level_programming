#!/usr/bin/python3
"""displays value of response header"""

from sys import argv
import requests


if __name__ == "__main__":
    print(requests.get(argv[1]).headers.get('x-Request-Id'))
