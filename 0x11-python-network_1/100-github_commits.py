#!/usr/bin/python3
"""start the code"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(sys.argv[2], sys.argv[1])).json()
    cont = 0
    for i in r:
        user_name = i.get('commit').get('author').get('name')
        print('{}: {}'.format(i.get('sha'), user_name))
        cont = cont + 1
        if cont > 9:
            break
