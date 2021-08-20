#!/usr/bin/python3
"""start the code"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    r = requests.get('https://api.github.com/user',
                     auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
