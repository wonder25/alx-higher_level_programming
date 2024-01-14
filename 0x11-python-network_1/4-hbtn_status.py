#!/usr/bin/python3
"""script that fetches url"""

import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    text = requests.get(url).text
    rtr_str = 'Body Response:\n\t- type: {}\n\t- content: {}'
    print(rtr_str.format(type(text), text))
