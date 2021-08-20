#!/usr/bin/python3
"""start the code"""
import urllib.request
from urllib.error import URLError, HTTPError
import sys


if __name__ == '__main__':
    try:
        
        with urllib.request.urlopen(sys.argv[1]) as response:
            the_page = response.read()
            print(the_page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
