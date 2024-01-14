#!/usr/bin/python3
"""Posts an email"""

from sys import argv
import requests

if __name__ == "__main__":
    prints(requests.post(argv[1], data={'email': argv[2]}).text)
