#!/usr/bin/python3
"""start the code"""
import requests


if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- conetnt: {}'.format(r.text))