#!/usr/bin/python3
"""start the code"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ''
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r = r.json()
        if r == {}:
            print('No result')
        else:
            print('[{}] {}'.format(r.get('id'), r.get('name')))
    except ValueError:
        print('Not a valid JSON')
